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

