-- SQL5 国庆期间每类视频点赞量和转发量
-- 较难  通过率：37.08%  时间限制：1秒  空间限制：256M
-- 描述
-- 用户-视频互动表tb_user_video_log
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
--    (101, 2001, '2021-09-24 10:00:00', '2021-09-24 10:00:20', 1, 1, 0, null)
--   ,(105, 2002, '2021-09-25 11:00:00', '2021-09-25 11:00:30', 0, 0, 1, null)
--   ,(102, 2002, '2021-09-25 11:00:00', '2021-09-25 11:00:30', 1, 1, 1, null)
--   ,(101, 2002, '2021-09-26 11:00:00', '2021-09-26 11:00:30', 1, 0, 1, null)
--   ,(101, 2002, '2021-09-27 11:00:00', '2021-09-27 11:00:30', 1, 1, 0, null)
--   ,(102, 2002, '2021-09-28 11:00:00', '2021-09-28 11:00:30', 1, 0, 1, null)
--   ,(103, 2002, '2021-09-29 11:00:00', '2021-09-29 11:00:30', 1, 0, 1, null)
--   ,(102, 2002, '2021-09-30 11:00:00', '2021-09-30 11:00:30', 1, 1, 1, null)
--   ,(101, 2001, '2021-10-01 10:00:00', '2021-10-01 10:00:20', 1, 1, 0, null)
--   ,(102, 2001, '2021-10-01 10:00:00', '2021-10-01 10:00:15', 0, 0, 1, null)
--   ,(103, 2001, '2021-10-01 11:00:50', '2021-10-01 11:01:15', 1, 1, 0, 1732526)
--   ,(106, 2002, '2021-10-02 10:59:05', '2021-10-02 11:00:05', 2, 0, 1, null)
--   ,(107, 2002, '2021-10-02 10:59:05', '2021-10-02 11:00:05', 1, 0, 1, null)
--   ,(108, 2002, '2021-10-02 10:59:05', '2021-10-02 11:00:05', 1, 1, 1, null)
--   ,(109, 2002, '2021-10-03 10:59:05', '2021-10-03 11:00:05', 0, 1, 0, null);
-- INSERT INTO tb_video_info(video_id, author, tag, duration, release_time) VALUES
--    (2001, 901, '旅游', 30, '2020-01-01 7:00:00')
--   ,(2002, 901, '旅游', 60, '2021-01-01 7:00:00')
--   ,(2003, 902, '影视', 90, '2020-01-01 7:00:00')
--   ,(2004, 902, '美女', 90, '2020-01-01 8:00:00');
-- 复制
-- 输出：
-- 旅游|2021-10-01|5|2
-- 旅游|2021-10-02|5|3
-- 旅游|2021-10-03|6|3
SELECT
  *
FROM
  (
    SELECT
      tag,
      dt,
      SUM(like_cnt) OVER w sum_like_cnt_7d,
      MAX(retweet_cnt) OVER w sum_retweet_cnt_7d
    FROM
      (
        SELECT
          tag,
          DATE(start_time) dt,
          SUM(if_like) like_cnt,
          SUM(if_retweet) retweet_cnt
        FROM
          tb_video_info
          LEFT JOIN tb_user_video_log USING(video_id)
        WHERE
          DATE(start_time) BETWEEN '2021-09-25'
          AND '2021-10-03'
        group by
          1,
          2
      ) t1 WINDOW w AS (
        PARTITION BY tag
        ORDER BY
          dt DESC ROWS BETWEEN CURRENT ROW
          AND 6 FOLLOWING
      )
  ) t2
GROUP BY
  1,
  2
HAVING
  dt BETWEEN '2021-10-01'
  AND '2021-10-03'
ORDER BY
  1 DESC,
  2 --2
select
  *
from
  (
    select
      tag,
      dt,
      sum(like_cnt) over(
        partition by tag
        order by
          dt rows 6 preceding
      ) sum_like_cnt_7d,
      max(retweet_cnt) over(
        partition by tag
        order by
          dt rows 6 preceding
      ) max_retweet_cnt_7d
    from
      (
        select
          tag,
          DATE(start_time) as dt,
          sum(if_like) as like_cnt,
          sum(if_retweet) as retweet_cnt
        from
          tb_video_info a
          left join tb_user_video_log b using (video_id)
        group BY
          1,
          2
      ) t1
  ) t2
where
  dt between '2021-10-01'
  and '2021-10-03'
order by
  1 desc,
  2