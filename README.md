test_1: Insert 20000 rows into items in one db session
test_2: Insert 20000 rows into warehouses in one db session
test_3: Insert 4000 rows into stocks in one db session
test_4: Insert 20000 rows into items row by row
test_5: Select from Items where i_price < 50
test_6: Select Distinct i_price from items
test_7: Select from Items where i_id <100
test_8: Select from Items where i_id <10000
test_9: Select from Items where i_id <19000
test_10: Select w_id, count(w_id)  from Stocks where w_id<1000 group by w_id
test_11: Select w_id, sum(quantity)  from Stocks where w_id<1000 group by w_id
test_12: Update i_name from Items
test_13: Select from Stocks left join Warehouses
test_14: Delete from Stocks
