-- 1-Qual é o endereço (carteira) com maior volume de transações enviadas?
-- R: Carteira A-83
-- Observação: "volume de transações" foi considerado como a soma do valor enviado.
WITH ranked_transactions AS 
(
  SELECT *, ROW_NUMBER() OVER (PARTITION BY IdTransaction ORDER BY ImportDate DESC) AS rn
  FROM db_hiring_test.raw_transactions_table
)
SELECT AddressOrigin, SUM(TotalSent) FROM ranked_transactions
WHERE rn = 1 AND status = 'Confirmed'
GROUP BY AddressOrigin ORDER BY SUM(TotalSent) DESC LIMIT 1;

-- 2-Qual é o dia do mês com maior volume de transações realizadas?
-- R: Dia 07
-- Observação: para esse caso optou-se por desconsiderar as transações negadas, considerando somente as transações confirmadas e pendentes.
WITH ranked_transactions AS 
(
  SELECT *, ROW_NUMBER() OVER (PARTITION BY IdTransaction ORDER BY ImportDate DESC) AS rn
  FROM db_hiring_test.raw_transactions_table
)
SELECT DAY(SentDate), SUM(TotalSent) FROM ranked_transactions
WHERE rn = 1 AND status <> 'Denied'
GROUP BY DAY(SentDate) ORDER BY SUM(TotalSent) DESC LIMIT 1;

-- 3-Em qual dia da semana geralmente mais transações são realizadas?
-- R: Quinta-feira
-- Observação: para esse caso optou-se por desconsiderar as transações negadas, considerando somente as transações confirmadas e pendentes.
WITH ranked_transactions AS 
(
  SELECT *, ROW_NUMBER() OVER (PARTITION BY IdTransaction ORDER BY ImportDate DESC) AS rn
  FROM db_hiring_test.raw_transactions_table
)
SELECT DAYOFWEEK(SentDate), AVG(TotalSent) FROM ranked_transactions
WHERE rn = 1 AND status <> 'Denied'
GROUP BY DAYOFWEEK(SentDate) ORDER BY AVG(TotalSent) DESC LIMIT 1;

-- 4-Quais transações possuem condições atípicas e precisam ser validadas com o time responsável pela disponibilização dos dados?
-- R: Transações cuja carteira de origem e destino são iguais, seria atípico pois esperava-se que a transação fosse o envio de valor de
-- uma carteira para outra. Outras questões atípicas podemos citar valores vazios para TotalSent bem como valores entre parênteses

SELECT * FROM ranked_transactions
WHERE AddressOrigin = AddressDestination;

SELECT * FROM ranked_transactions
ORDER BY TotalSent;

-- 5- Qual a carteira com o maior saldo final? (considere que todas as carteiras estejam zeradas no
-- início das análises e que seja possível existir saldo negativo).
-- R: Foi criado um SELECT que lista todas as carteiras atuais sem duplicidade e seus atuais valores enviados e recebidos para que
-- seja realizado o cálculo de valor atual a partir dos enviados e recebidos.
-- De acordo com a query abaixo a carteira com maior saldo final seria a carteira A-30

WITH ranked_transactions AS 
(
  SELECT *, ROW_NUMBER() OVER (PARTITION BY IdTransaction ORDER BY ImportDate DESC) AS rn
  FROM db_hiring_test.raw_transactions_table
), 
sent_values AS 
(
    SELECT AddressOrigin AS Address, SUM(TotalSent) AS TotalSent FROM ranked_transactions
    WHERE rn = 1 AND status = 'Confirmed'
    GROUP BY AddressOrigin
),
received_value AS
(
    SELECT AddressDestination AS Address, SUM(TotalSent) AS TotalReceived FROM ranked_transactions
    WHERE rn = 1 AND status = 'Confirmed'
    GROUP BY AddressDestination
),
addresses AS
(
    SELECT Address FROM sent_values
    UNION
    SELECT Address FROM received_value 
)
SELECT a.Address, rv.TotalReceived, sv.TotalSent, (rv.TotalReceived - sv.TotalSent) AS CurrentAddressValue
    FROM addresses a
LEFT JOIN received_value rv ON a.Address = rv.Address
LEFT JOIN sent_values sv ON a.Address = sv.Address
ORDER BY CurrentAddressValue DESC LIMIT 1;

