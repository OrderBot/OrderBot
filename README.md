**OrderBot**
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Given scope is an “Invoice (order and inventory) processing” system. Considering this in mind, this assignment has been prototyped and developed like a complete real time inventory processing system in all aspects.  Below are the salient features of this design.
<br><br>
<b>Designed an intelligent Order Processing system capable of processing multiple invoices simultaneously.</b>
<br>
Developed confirming to Publisher-Subscriber design pattern 
<br>
1.	Publisher  (Order receiver) – Itself confirms to factory pattern
<br>
2.	Subscriber (Order Processor) – Simple OOAD
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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;o	Example:- Inbound orders are read from  “inbound_orders/ order_cust*.json” in code. This can be changed via config file<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	Magical way of running. No need to call any main scripts. Just call the current directory.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	Each order has been allocated with UUID. Hence even two different orders with same header will be treated unique.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	Imports are aligned per PEP8. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I.  First python STL, <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;II.  then 3rd party <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;III.  then local imports<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•	Intelligent rotating logger, with 5MB of max size and backup count of 5. But still this is configurable via config file. Change it as you wish.<br>
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
