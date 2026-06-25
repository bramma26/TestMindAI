# TestMind AI - Database Design

## Table: requirements

| Column           | Type     |
| ---------------- | -------- |
| id               | Integer  |
| requirement_text | Text     |
| created_at       | Datetime |

## Table: test_cases

| Column          | Type    |
| --------------- | ------- |
| id              | Integer |
| requirement_id  | Integer |
| scenario        | Text    |
| test_case       | Text    |
| expected_result | Text    |

## Table: users

| Column   | Type    |
| -------- | ------- |
| id       | Integer |
| username | Varchar |
| email    | Varchar |
| password | Varchar |

