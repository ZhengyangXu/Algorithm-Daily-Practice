-- SQL8 每 篇 文 章 同 一 时 刻 最 大 在 看 人 数 题 目 题 解(23) 讨 论(31) 排 行 中 等 通 过 率 ： 35.46 % 时 间 限 制 ： 1 秒 空 间 限 制 ： 256M 描 述 用 户 行 为 日 志 表 tb_user_log id uid artical_id in_time out_time sign_cin 1 101 9001 2021 -11 -01 10 :00 :00 2021 -11 -01 10 :00 :11 0 2 102 9001 2021 -11 -01 10 :00 :09 2021 -11 -01 10 :00 :38 0 3 103 9001 2021 -11 -01 10 :00 :28 2021 -11 -01 10 :00 :58 0 4 104 9002 2021 -11 -01 11 :00 :45 2021 -11 -01 11 :01 :11 0 5 105 9001 2021 -11 -01 10 :00 :51 2021 -11 -01 10 :00 :59 0 6 106 9002 2021 -11 -01 11 :00 :55 2021 -11 -01 11 :01 :24 0 7 107 9001 2021 -11 -01 10 :00 :01 2021 -11 -01 10 :01 :50 0 （ uid - 用 户 ID,
-- artical_id - 文 章 ID,
-- in_time - 进 入 时 间,
-- out_time - 离 开 时 间,
-- sign_in - 是 否 签 到 ） 场 景 逻 辑 说 明 ： artical_id - 文 章 ID 代 表 用 户 浏 览 的 文 章 的 ID ， artical_id - 文 章 ID 为 0 表 示 用 户 在 非 文 章 内 容 页 （ 比 如 App 内 的 列 表 页 、 活 动 页 等 ） 。 问 题 ： 统 计 每 篇 文 章 同 一 时 刻 最 大 在 看 人 数 ， 如 果 同 一 时 刻 有 进 入 也 有 离 开 时 ， 先 记 录 用 户 数 增 加 再 记 录 减 少 ， 结 果 按 最 大 人 数 降 序 。 输 出 示 例 ： 示 例 数 据 的 输 出 结 果 如 下 artical_id max_uv 9001 3 9002 2 解 释 ： 10 点 0 分 10 秒 时 ， 有 3 个 用 户 正 在 浏 览 文 章 9001 ； 11 点 01 分 0 秒 时 ， 有 2 个 用 户 正 在 浏 览 文 章 9002 。 示 例 1 输 入 ： DROP TABLE IF EXISTS tb_user_log;
-- CREATE TABLE tb_user_log (
--   id INT PRIMARY KEY AUTO_INCREMENT COMMENT '自增ID',
--   uid INT NOT NULL COMMENT '用户ID',
--   artical_id INT NOT NULL COMMENT '视频ID',
--   in_time datetime COMMENT '进入时间',
--   out_time datetime COMMENT '离开时间',
--   sign_in TINYINT DEFAULT 0 COMMENT '是否签到'
-- ) CHARACTER SET utf8 COLLATE utf8_bin;
-- INSERT INTO
--   tb_user_log(uid, artical_id, in_time, out_time, sign_in)
-- VALUES
--   (
--     101,
--     9001,
--     '2021-11-01 10:00:00',
--     '2021-11-01 10:00:11',
--     0
--   ),
--   (
--     102,
--     9001,
--     '2021-11-01 10:00:09',
--     '2021-11-01 10:00:38',
--     0
--   ),
--   (
--     103,
--     9001,
--     '2021-11-01 10:00:28',
--     '2021-11-01 10:00:58',
--     0
--   ),
--   (
--     104,
--     9002,
--     '2021-11-01 11:00:45',
--     '2021-11-01 11:01:11',
--     0
--   ),
--   (
--     105,
--     9001,
--     '2021-11-01 10:00:51',
--     '2021-11-01 10:00:59',
--     0
--   ),
--   (
--     106,
--     9002,
--     '2021-11-01 11:00:55',
--     '2021-11-01 11:01:24',
--     0
--   ),
--   (
--     107,
--     9001,
--     '2021-11-01 10:00:01',
--     '2021-11-01 10:01:50',
--     0
--   );
-- 复 制 输 出 ： 9001 | 3 9002 | 2
select
  artical_id,
  max(instant_viewr) max_uv
from
  (
    select
      artical_id,,
      sum(diff) over(
        partition by artical_id
        order by
          tm,
          diff desc
      ) as instant_viewr (
        select
          artical_id,
          in_time tm,
          1 diff
        from
          tb_user_log
        union all
        select
          artical_id,
          out_time tm,
          -1 diff
        from
          tb_user_log
      ) t1
  ) t2
group by
  1
order by
  2 desc