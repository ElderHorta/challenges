------------------------------------------------------------
-- 1-Considerando que a carteira origem é responsável por pagar as taxas de envio, qual carteira
-- seria responsável pelo maior pagamento de taxas em janeiro de 2021?
-- R: Carteira A-99.
-- Obs: estamos desconsiderando valores entre parênteses que devem ser avalaidos com a área de negócios
WITH ranked_transactions AS 
(
  SELECT *, ROW_NUMBER() OVER (PARTITION BY IdTransaction ORDER BY ImportDate DESC) AS rn
  FROM db_hiring_test.raw_transactions_table
),
transactions AS
(
    SELECT AddressOrigin, 
        CAST(REGEXP_REPLACE(TotalSent, '[,()]+', '') AS DECIMAL(10,2)) AS FixedTotalSent, 
        `fee-percentage`
    FROM ranked_transactions tab
    LEFT JOIN db_hiring_test.raw_transactions_fee fee 
        ON CAST(REGEXP_REPLACE(TotalSent, '[,()]+', '') AS DECIMAL(10,2)) 
            >= CAST(fee.`range-start` AS DECIMAL(10,2)) 
        AND CAST(REGEXP_REPLACE(TotalSent, '[,()]+', '') AS DECIMAL(10,2)) 
            <= CAST(fee.`range-end` AS DECIMAL(10,2))
    WHERE tab.rn = 1 AND tab.status = 'Confirmed' AND SentDate >= '2021-01-01' AND SentDate < '2021-02-01'
)
SELECT AddressOrigin, SUM(FixedTotalSent * `fee-percentage` / 100) AS fee  FROM transactions
GROUP BY AddressOrigin
ORDER BY fee DESC LIMIT 1;

-- 2- E em fevereiro de 2021?
-- R: Carteira A-29
WITH ranked_transactions AS 
(
  SELECT *, ROW_NUMBER() OVER (PARTITION BY IdTransaction ORDER BY ImportDate DESC) AS rn
  FROM db_hiring_test.raw_transactions_table
),
transactions AS
(
    SELECT AddressOrigin, 
        CAST(REGEXP_REPLACE(TotalSent, '[,()]+', '') AS DECIMAL(10,2)) AS FixedTotalSent, 
        `fee-percentage`
    FROM ranked_transactions tab
    LEFT JOIN db_hiring_test.raw_transactions_fee fee 
        ON CAST(REGEXP_REPLACE(TotalSent, '[,()]+', '') AS DECIMAL(10,2)) >= CAST(fee.`range-start` AS DECIMAL(10,2)) 
        AND CAST(REGEXP_REPLACE(TotalSent, '[,()]+', '') AS DECIMAL(10,2)) <= CAST(fee.`range-end` AS DECIMAL(10,2))
    WHERE tab.rn = 1 AND tab.status = 'Confirmed' AND SentDate >= '2021-02-01' AND SentDate < '2021-03-01'
)
SELECT AddressOrigin, SUM(FixedTotalSent * `fee-percentage` / 100) AS fee  FROM transactions
GROUP BY AddressOrigin
ORDER BY fee DESC LIMIT 1;

-- 3- Qual é o id da transação com a maior taxa paga?
-- R: ID635
WITH ranked_transactions AS 
(
  SELECT *, ROW_NUMBER() OVER (PARTITION BY IdTransaction ORDER BY ImportDate DESC) AS rn
  FROM db_hiring_test.raw_transactions_table
),
transactions AS
(
    SELECT IdTransaction,
        CAST(REGEXP_REPLACE(TotalSent, '[,()]+', '') AS DECIMAL(10,2)) AS FixedTotalSent, 
        `fee-percentage`
    FROM ranked_transactions tab
    LEFT JOIN db_hiring_test.raw_transactions_fee fee 
        ON CAST(REGEXP_REPLACE(TotalSent, '[,()]+', '') AS DECIMAL(10,2)) 
            >= CAST(fee.`range-start` AS DECIMAL(10,2)) 
        AND CAST(REGEXP_REPLACE(TotalSent, '[,()]+', '') AS DECIMAL(10,2)) 
            <= CAST(fee.`range-end` AS DECIMAL(10,2))
    WHERE tab.rn = 1 AND tab.status = 'Confirmed'
)
SELECT IdTransaction, FixedTotalSent, `fee-percentage`, (FixedTotalSent * `fee-percentage` / 100) AS fee  FROM transactions
ORDER BY fee  DESC LIMIT 1;

-- 4- Qual é a média de taxa paga considerando todas as transações realizadas?
-- R: 21713,05.
WITH ranked_transactions AS 
(
  SELECT *, ROW_NUMBER() OVER (PARTITION BY IdTransaction ORDER BY ImportDate DESC) AS rn
  FROM db_hiring_test.raw_transactions_table
),
transactions AS
(
    SELECT CAST(REGEXP_REPLACE(TotalSent, '[,()]+', '') AS DECIMAL(10,2)) AS FixedTotalSent, 
        `fee-percentage`
    FROM ranked_transactions tab
    LEFT JOIN db_hiring_test.raw_transactions_fee fee 
        ON CAST(REGEXP_REPLACE(TotalSent, '[,()]+', '') AS DECIMAL(10,2)) 
            >= CAST(fee.`range-start` AS DECIMAL(10,2)) 
        AND CAST(REGEXP_REPLACE(TotalSent, '[,()]+', '') AS DECIMAL(10,2)) 
            <= CAST(fee.`range-end` AS DECIMAL(10,2))
    WHERE tab.rn = 1 AND tab.status = 'Confirmed'
)
SELECT AVG(FixedTotalSent * `fee-percentage` / 100) AS fee  FROM transactions
ORDER BY fee  DESC LIMIT 1;
