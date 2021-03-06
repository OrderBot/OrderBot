#**OrderBot**
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Given scope is an “Invoice (order and inventory) processing” system. Considering this in mind, this project has been prototyped and developed like a complete real time inventory processing system in all aspects.  Below are the salient features of this design.
<br><br>
<b>Designed an intelligent Order Processing system capable of processing multiple invoices simultaneously.</b>
<br>
Developed to match Publisher-Subscriber pattern. Being proto type this implementation is made simple on the code without introducing any async messaging libraries like CELERY. Keeping ReaderFactory as publisher as it reads the order from DB and directly puts in to the subscriber which is InventoryAllocator, by employing multiprocessing queue in between them.
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.	Publisher  (Order receiver) – Itself confirms to factory pattern
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.	Subscriber (Order Processor) – Simple OOAD
<br><br>
The implementation classes(DistributedReader.py, CloudReader.py.......) that are not completed are not left as it is. They have been added with plain english text pesudo-code/steps. Necessary libraries like PyHive, requests, boto are mentioned in the pseudo code.
<br>Config file has attributes for all of them
<br><br>
<b><i>Aim:- </b></i>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Order processing system can read multiple orders simultaneously from DB and process them parallel.
<br><br>
<b><i>Code Design:- </b></i>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Avoided DB due to time constraint and being a proto type model. But kept “files stream” for this scope. As described below
All incoming orders will be placed in a directory called inbound_orders. Designed such a way that this path can be configured via config file, hence flexible to keep any. Each JSON file in this folder is considered as individual order from different customer.  Hence order processor will spawn as many processes as total of all orders read from all these files. If this list exceed “MAX_PROCESS”, then we will stick with the  MAX_PROCESS. Entire list of JSON orders will be then segmented equal to MAX_PROCESS
<br><br>
<b><i>Salient Features:- </b></i>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	Has it’s own config file. Hence many parameters can be passed to the project via setting them in config file. Not necessary to change the code. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o	Example:- Inbound orders are read from  "inbound_orders/order_cust\*.json" in code. This can point to any path that we can set in config file<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	Magical way of running. No need to call any main scripts. Just call the current directory.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	Each order has been allocated with UUID. Hence even two different orders with same header will be treated unique.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	Imports are aligned per PEP8. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I.  First python STL, <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;II.  then 3rd party <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;III.  then local imports<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	Intelligent rotating logger, with 5MB of max size and backup count of 5. But still this is configurable via config file. Change it as you wish.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	Intelligent command line main module with GNU style command line options and help message.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	Self is selfish, hence using “this” pointer. ☺ ☺ ☺ ☺ <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	Made use of iter() in possible places while handling lists/tuples for memory efficiency. This makes looping with less memory usage instead loading entire array in memory<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	No more hard coding like if key == "Header", MACRO’s have been used which makes code much optimized. Hence any point if those names changes from “Header” to “Footer”, then all it takes just to change the MACRO, not a grep and replace thru entire source code.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	If a customer requests an invalid order like “H”, then will skip current order and proceed to next order.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	Used return codes instead of plain return of success/failure. This makes more sense.<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	Just used some funny messages, if you are really a serious guy, please please please pardon me.<br>
<br><br>
<b><i>Directory Structure:- </b></i>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── BaseDB<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── Config<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── InventoryProcessor<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── OrderReader<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── Utils<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── inbound_orders<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── logs<br>
<br><br>
<b><i>Details:-</b></i>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>BaseDB:-</b></i>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Database to hold ware house inventory. As of now being file stream considered for this scope, it has the JSON file(ware_house.json) as ware house stock data.
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>Config:-</b></i>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Config file for the project
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>InventoryProcessor:-</b></i>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Business logic to allocate oncoming  orders from ware house.
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>OrderReader:-</b></i>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Business logic to read orders from different streams. Streams in         current scope 
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FileStreamReader.py     → reads from JSON file
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NetworkStreamReader.py → reads from Network(only template, not implemented)
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DBStreamReader.py → reads from DB(only template, not implemented)
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DistributedReader.py → Reads from Hadoop (only template, not implemented)
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ElasticDBReader.py → Reads from Elastic Server (only template, not implemented)
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CloudReader.py → Reads from Amazon Cloud (only template, not implemented)
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>Utils:-</b></i>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All utility modules
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>inbound_orders:-</b></i>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Incoming orders from customers
<br><br>
<b><i>How to Run:-</b></i><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Place your input orders in “inbound_orders” directory with a name “order_cust*.json”.For immediate test run already have some orders placed here. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Check the warehouse database(below JSON file) to make sure we have inventory.For immediate test run, already populated ware_house.json with stock<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>BaseDB/ware_house.json</b></i><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Run the directory, as in step 4. Yes of course, coz when we run the application we just double click the icon and run it. So just to get this resemblance this approach has been made<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. cd to the project root. Run the below command<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>python . File -i ./inbound_orders</b></i>
<br><br>
<b><i>Considerations:-</b></i>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➢	Valid Order(since A met the criteria): <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{"Header": 1, "Lines": {"Product": "A", "Quantity": "1"}{"Product": "C", "Quantity": "0"}} <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➢	Invalid Order:- <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{"Header": 1, "Lines": {"Product": "D", "Quantity": "6"}} <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➢	Final Output of the run will be in below JOSN format. This is because the format can be used as commit logs which is help full to retrieve any order info at later point of time, based on the UUID.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>Final Output(will be a JSON array):-</b></i><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UUID: [<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“Header” : <value>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“OrderedProduct”: <value>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“OrderDetails:  (Requested, Processed, BackOrdered)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“Header” : <value>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“OrderedProduct”: <value>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“OrderDetails:  (Requested, Processed, BackOrdered)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UUID: [<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“Header” : <value>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“OrderedProduct”: <value>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“OrderDetails:  (Requested, Processed, BackOrdered)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“Header” : <value>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“OrderedProduct”: <value>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“OrderDetails:  (Requested, Processed, BackOrdered)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➢	For any given item, available stock should not be zero and should be grater than requested order. If this criterion is not met for any current order, current item will be backordered and will proceed to next order. We will continue until stock becomes lesser than the quantity requested or becomes empty, whichever occurs first.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➢	Inventory is kept in a json file as of now. Better scope is DB. All processes simultaneously access this file. Code is made sure that every process updates the file as per the inventory it processed, so that next process will continue from where last process left it. So when you run the application continuously, you can observe that the stock is getting reduced gradually.<br>

