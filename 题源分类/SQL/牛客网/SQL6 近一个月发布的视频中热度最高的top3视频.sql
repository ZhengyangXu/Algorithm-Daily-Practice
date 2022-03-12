-- SQL6 近一个月发布的视频中热度最高的top3视频
-- 困难  通过率：24.66%  时间限制：1秒  空间限制：256M
-- 描述
-- 现有用户-视频互动表tb_user_video_log
-- 问题：找出近一个月发布的视频中热度最高的top3视频。
-- 注：
-- 热度=(a*视频完播率+b*点赞数+c*评论数+d*转发数)*新鲜度；
-- 新鲜度=1/(最近无播放天数+1)；
-- 当前配置的参数a,b,c,d分别为100、5、3、2。
-- 最近播放日期以end_time-结束观看时间为准，假设为T，则最近一个月按[T-29, T]闭区间统计。
-- 结果中热度保留为整数，并按热度降序排序。
-- 输出示例：
-- 示例数据的输出结果如下
-- video_id	hot_index
-- 2001	122
-- 2002	56
-- 2003	1
-- 解释：
-- 最近播放日期为2021-10-03，记作当天日期；近一个月（2021-09-04及之后）发布的视频有2001、2002、2003、2004，不过2004暂时还没有播放记录；
-- 视频2001完播率1.0（被播放次数4次，完成播放4次），被点赞3次，评论1次，转发2次，最近无播放天数为0，因此热度为：(100*1.0+5*3+3*1+2*2)/(0+1)=122
-- 同理，视频2003完播率0，被点赞数1，评论和转发均为0，最近无播放天数为3，因此热度为：(100*0+5*1+3*0+2*0)/(3+1)=1（1.2保留为整数）。
-- 示例1
-- 输入：
-- DROP TABLE IF EXISTS tb_user_video_log, tb_video_info;
-- CREATE TABLE tb_user_video_log (
--     id INT PRIMARY KEY AUTO_INCREMENT COMMENT '自增ID',
--     uid INT NOT NULL COMMENT '用户ID',
--     video_id INT NOT NULL COMMENT '视频ID',
--     start_time datetime COMMENT '开始观看时间',
--     end_time datetime COMMENT '结束观看时间',
--     if_follow TINYINT COMMENT '是否关注',
--     if_like TINYINT COMMENT '是否点赞',
--     if_retweet TINYINT COMMENT '是否转发',
--     comment_id INT COMMENT '评论ID'
-- ) CHARACTER SET utf8 COLLATE utf8_bin;
-- CREATE TABLE tb_video_info (
--     id INT PRIMARY KEY AUTO_INCREMENT COMMENT '自增ID',
--     video_id INT UNIQUE NOT NULL COMMENT '视频ID',
--     author INT NOT NULL COMMENT '创作者ID',
--     tag VARCHAR(16) NOT NULL COMMENT '类别标签',
--     duration INT NOT NULL COMMENT '视频时长(秒数)',
--     release_time datetime NOT NULL COMMENT '发布时间'
-- )CHARACTER SET utf8 COLLATE utf8_bin;
-- INSERT INTO tb_user_video_log(uid, video_id, start_time, end_time, if_follow, if_like, if_retweet, comment_id) VALUES
--    (101, 2001, '2021-09-24 10:00:00', '2021-09-24 10:00:30', 1, 1, 1, null)
--   ,(101, 2001, '2021-10-01 10:00:00', '2021-10-01 10:00:31', 1, 1, 0, null)
--   ,(102, 2001, '2021-10-01 10:00:00', '2021-10-01 10:00:35', 0, 0, 1, null)
--   ,(103, 2001, '2021-10-03 11:00:50', '2021-10-03 11:01:35', 1, 1, 0, 1732526)
--   ,(106, 2002, '2021-10-02 10:59:05', '2021-10-02 11:00:04', 2, 0, 1, null)
--   ,(107, 2002, '2021-10-02 10:59:05', '2021-10-02 11:00:06', 1, 0, 0, null)
--   ,(108, 2002, '2021-10-02 10:59:05', '2021-10-02 11:00:05', 1, 1, 1, null)
--   ,(109, 2002, '2021-10-03 10:59:05', '2021-10-03 11:00:01', 0, 1, 0, null)
--   ,(105, 2002, '2021-09-25 11:00:00', '2021-09-25 11:00:30', 1, 0, 1, null)
--   ,(101, 2003, '2021-09-26 11:00:00', '2021-09-26 11:00:30', 1, 0, 0, null)
--   ,(101, 2003, '2021-09-30 11:00:00', '2021-09-30 11:00:30', 1, 1, 0, null);
-- INSERT INTO tb_video_info(video_id, author, tag, duration, release_time) VALUES
--    (2001, 901, '旅游', 30, '2021-09-05 7:00:00')
--   ,(2002, 901, '旅游', 60, '2021-09-05 7:00:00')
--   ,(2003, 902, '影视', 90, '2021-09-05 7:00:00')
--   ,(2004, 902, '影视', 90, '2021-09-05 8:00:00');
-- 复制
-- 输出：
-- 2001|122
-- 2002|56
-- 2003|1
SELECT
  video_id,
  ROUND(
    (
      100 * finished_rate + 5 * like_cnt + 3 * comment_count + 2 * retweet_cnt
    ) / (unfinished_day_cnt + 1)
  ) hot_index
FROM
  (
    SELECT
      i.video_id,
      SUM(
        TIMESTAMPDIFF(second, start_time, end_time) >= duration
      ) / COUNT(*) finished_rate,
      SUM(if_like = 1) like_cnt,
      SUM(IF(comment_id IS NOT NULL, 1, 0)) comment_count,
      SUM(if_retweet = 1) retweet_cnt,
      DATEDIFF(
        DATE(
          (
            SELECT
              MAX(end_time)
            FROM
              tb_user_video_log
          )
        ),
        MAX(DATE(end_time))
      ) unfinished_day_cnt
    FROM
      tb_video_info i
      JOIN tb_user_video_log USING(video_id)
    WHERE
      DATEDIFF(
        DATE(
          (
            SELECT
              MAX(end_time)
            FROM
              tb_user_video_log
          )
        ),
        DATE(release_time)
      ) <= 29
    GROUP BY
      1
  ) t
ORDER BY
  2 DESC
LIMIT
  3
SELECT
  video_id,
  ROUND(
    (
      100 * comp_play_rate + 5 * like_cnt + 3 * comment_cnt + 2 * retweet_cnt
    ) / (
      TIMESTAMPDIFF(DAY, recently_end_date, cur_date) + 1
    ),
    0
  ) as hot_index
FROM
  (
    SELECT
      video_id,
      AVG(
        IF(
          TIMESTAMPDIFF(SECOND, start_time, end_time) >= duration,
          1,
          0
        )
      ) as comp_play_rate,
      SUM(if_like) as like_cnt,
      COUNT(comment_id) as comment_cnt,
      SUM(if_retweet) as retweet_cnt,
      MAX(DATE(end_time)) as recently_end_date,
      -- 最近被播放日期
      MAX(DATE(release_time)) as release_date,
      -- 发布日期
      MAX(cur_date) as cur_date -- 非分组列，加MAX避免语法错误
    FROM
      tb_user_video_log
      JOIN tb_video_info USING(video_id)
      LEFT JOIN (
        SELECT
          MAX(DATE(end_time)) as cur_date
        FROM
          tb_user_video_log
      ) as t_max_date ON 1
    GROUP BY
      video_id
    HAVING
      TIMESTAMPDIFF(DAY, release_date, cur_date) < 30
  ) as t_video_info
ORDER BY
  hot_index DESC
LIMIT
  3;