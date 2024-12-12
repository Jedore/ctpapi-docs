<span class="anchor" id="3e7c9c0e-ac9c-400c-954c-8e48141bf277"></span>
## 1. 报单
<span class="anchor" id="20943aba-64a5-4714-be80-8bbe4a32e8c3"></span>
### 1.1. FrontID + SessionID + OrderRef  
<p>当报单报入CTP后，这组序号可以唯一定位一笔报单。可以用于跟踪报单回报的整个生命周期，但无法跟踪成交回报，因为成交回报里没有这组序号。  </p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配，即对于同一笔报单，清流重启前后的这组序号会不一致，使用上需注意。</p>
<span class="anchor" id="e106096f-1e58-4f49-a935-014d480b3035"></span>
### 1.2. ExchangeID + TraderID + OrderLocalID  
<p>当报单被CTP接受后，系统会分配OrderLocalID并发往交易所，这组序号可以用于跟踪此后报单的生命周期，包括报单回报和成交回报。</p>
<p>当报单被CTP拒绝后，不会分配OrderLocalID，此时仍要使用第1组序号跟踪报单。</p>
<p>注意：CTP清流重启后报单回报中的该组序号保持不变。</p>
<span class="anchor" id="335ad963-2065-4cbf-969e-34b5f3911bd7"></span>
### 1.3. ExchangeID + OrderSysID  
<p>当报单被交易所接受后，交易所系统会分配OrderSysID并给CTP推送报单回报，这组序号可以用于跟踪此后报单的生命周期，包括报单回报和成交回报。</p>
<p>当报单被交易所拒绝后，交易所不会分配OrderSysID，此时仍要使用第1和第2组序号跟踪报单。</p>
<p>注意：CTP清流重启后报单回报中的该组序号保持不变。</p>
<span class="anchor" id="d11f8a60-ad8c-4eb9-9405-2a5e3d105ade"></span>
### 1.4. RequestID
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a>中的RequestID与<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的相对应，可以用于跟踪报单回报的整个生命周期，但无法跟踪成交回报，因为成交回报里没有这个字段。</p>
<p>注意：CTP清流重启后该序号置零。</p>
<span class="anchor" id="b7dc4f9a-c777-40ba-bd60-fdb531d0264f"></span>
### 1.5. RelativeOrderSysID
<p>用于关联条件报单和触发后的报单回报。当报入条件单后，会生成OrderSysID=TJBD_XX的报单，此时状态为未触发；当行情满足条件并触发条件单后，会生成一笔新的报单，其RelativeOrderSysID=TJBD_XX。</p>
<p>注意：CTP清流重启后RelativeOrderSysID会清空，无法再关联条件单。</p>
<span class="anchor" id="3aa9291f-a7b6-4d23-8afd-cf9356456978"></span>
## 2. 报价
<span class="anchor" id="256ccdb5-8147-48f0-878f-ac0af51df1fa"></span>
### 2.1. FrontID + SessionID + QuoteRef
<p>当报价报入CTP后，这组序号可以唯一定位一笔报价。可以用于跟踪报价回报的整个生命周期，但无法跟踪报价衍生单，因为报价衍生单回报（<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>和<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a>）里没有这组序号。  </p>
<p>注意：CTP清流重启后报价中的该组序号会重新分配，即对于同一笔报价，清流重启前后的这组序号会不一致，使用上需注意。</p>
<span class="anchor" id="a9d54a9a-edc4-459f-814f-79768f7d0b67"></span>
### 2.2. FrontID + SessionID + AskOrderRef/BidOrderRef  
<p>当报价报入CTP后，可以通过报价回报中的这组序号跟踪报价衍生单，AskOrderRef对应报价衍生卖单的OrderRef，BidOrderRef对应报价衍生买单的OrderRef。规则同上面报单接口的序号1。</p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配。</p>
<span class="anchor" id="06462365-8210-4637-b57b-30d2e4800ff5"></span>
### 2.3. ExchangeID + TraderID + QuoteLocalID
<p>当报价被CTP接受后，系统会分配QuoteLocalID并发往交易所，这组序号可以用于跟踪此后报价的生命周期，但无法跟踪报价衍生单，因为报价衍生单回报里没有这组序号。衍生单的序号规则同上面报价接口序号2。</p>
<p>当报价被CTP拒绝后，不会分配QuoteLocalID，此时仍要使用第1组序号跟踪报价。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="0abea8af-c370-4c83-b642-bda0fe0beb26"></span>
### 2.4. ExchangeID + QuoteSysID
<p>当报价被交易所接受后，交易所系统会分配QuoteSysID并给CTP推送报价回报，这组序号可以用于跟踪此后报价的生命周期，但无法跟踪报价衍生单，因为报价衍生单回报里没有这组序号。</p>
<p>当报价被交易所拒绝后，交易所不会分配QuoteSysID，此时仍要使用第1和第3组序号跟踪报价。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="6f6ac75f-2843-449c-a3b1-455aad01e5a8"></span>
### 2.5. ExchangeID + AskOrderSysID/BidOrderSysID
<p>当报价被交易所接受后，上期所、能源中心、中金所可以通过报价回报中的这组序号跟踪报价衍生单，AskOrderSysID对应报价衍生卖单的OrderSysID，BidOrderSysID对应报价衍生买单的OrderSysID。衍生单的序号规则同上面报单接口。</p>
<p>大商所和郑商所的报价回报中，AskOrderSysID和BidOrderSysID为空。</p>
<p>大商所报价回报中QuoteSysID对应买衍生单的的OrderSysID，QuoteSysID+1的值对应卖衍生单的OrderSysID，比如报价回报中QuoteSysID为110，那么衍生单的OrderSysID分别是110和111。</p>
<p>郑商所报价回报中QuoteSysID的前缀加上'a'对应卖衍生单的OrderSysID，QuoteSysID的前缀加上'b'对应买衍生单的OrderSysID，比如报价回报的QuoteSysID为110，那么衍生单的OrderSysID分别是a110、b110。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="29562e64-3d2a-4803-9a2f-34d98d4af988"></span>
### 2.6. RequestID
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQQUOTEINSERT/">ReqQuoteInsert</a>中的RequestID与<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNQUOTE/">OnRtnQuote</a>和<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的相对应，用于跟踪报价回报和报价衍生单回报的整个生命周期。例如<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQQUOTEINSERT/">ReqQuoteInsert</a>中RequestID=888，则<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNQUOTE/">OnRtnQuote</a>的RequestID=888，买衍生单的<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的RequestID=888，卖衍生单<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的RequestID=888。</p>
<p>注意：CTP清流重启后该序号置零。</p>
<span class="anchor" id="62fe6847-82df-4237-9ead-26e1284eef02"></span>
## 3. 询价
<span class="anchor" id="f40dd953-bc3d-4b98-a42b-af61a4eec231"></span>
### 3.1. ForQuoteRef
<p>当询价请求报入CTP后，该字段用来唯一定位一笔询价。</p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配。</p>
<span class="anchor" id="1101abd6-d53f-4be7-9616-f7e347ccfde3"></span>
### 3.2. ForQuoteSysID
<p>当询价被交易所接受后，交易所系统分配ForQuoteSysID，可以用于跟踪此后询价的的生命周期。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="69ccbe40-67aa-459e-98d2-e99b90c96525"></span>
## 4. 行权
<span class="anchor" id="31dbd3ce-4136-412d-84d1-84ec70e5895a"></span>
### 4.1. FrontID + SessionID + ExecOrderRef
<p>当行权请求报入CTP后，该组序号用来唯一定位一笔行权。</p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配。</p>
<span class="anchor" id="02f1b0a9-d951-4077-9f97-9e95b18fd1de"></span>
### 4.2. ExchangeID + TraderID + ExecOrderLocalID
<p>当行权被CTP接受后，可以通过行权回报中的这组序号跟踪此后行权的生命周期。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="17524532-3dad-4608-a766-823e24a5e38d"></span>
### 4.3. ExchangeID + ExecOrderSysID
<p>当行权被交易所接受后，可以通过行权回报中的这组序号跟踪此后行权的生命周期。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="5630647c-5c71-4e8d-8100-e7f6c6a82660"></span>
## 5. 自对冲
<span class="anchor" id="04b72563-f4dc-4225-86cc-5d5c3bfa42a9"></span>
### 5.1. FrontID + SessionID + OptionSelfCloseRef
<p>当自对冲报入CTP后，这组序号可以唯一定位一笔自对冲。可以用于跟踪自对冲回报的整个生命周期。  </p>
<p>注意：CTP清流重启后自对冲中的该组序号会重新分配，即对于同一笔自对冲，清流重启前后的这组序号会不一致，使用上需注意。</p>
<span class="anchor" id="2a535a47-af36-4d94-af1f-8f906ef5af0b"></span>
### 5.2. ExchangeID + TraderID + OptionSelfCloseLocalID
<p>当自对冲被CTP接受后，系统会分配OptionSelfCloseLocalID并发往交易所，这组序号可以用于跟踪此后自对冲的生命周期。</p>
<p>当自对冲被CTP拒绝后，不会分配OptionSelfCloseLocalID，此时仍要使用第1组序号跟踪自对冲。</p>
<p>注意：CTP清流重启后自对冲回报中的该组序号保持不变。</p>
<span class="anchor" id="5b89b158-b42a-4545-8bac-f73aa305ded3"></span>
### 5.3. ExchangeID + OptionSelfCloseSysID
<p>当自对冲被交易所接受后，交易所系统会分配OptionSelfCloseSysID并给CTP推送自对冲回报，这组序号可以用于跟踪此后自对冲的生命周期。</p>
<p>当自对冲被交易所拒绝后，交易所不会分配OptionSelfCloseSysID，此时仍要使用第1和第2组序号跟踪自对冲。</p>
<p>注意：CTP清流重启后自对冲回报中的该组序号保持不变。</p>
<blockquote>
<p>大商所不适用此序号，因为大商所不分配OptionSelfCloseSysID值。</p>
</blockquote>
<span class="anchor" id="fa445285-19cd-4bf1-8e81-7c807f24b17c"></span>
### 5.4. RequestID
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEINSERT/">ReqOptionSelfCloseInsert</a>中的RequestID与<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNOPTIONSELFCLOSE/">OnRtnOptionSelfClose</a>中的相对应，用于跟踪自对冲回报的整个生命周期。</p>
<p>注意：CTP清流重启后该序号置零。</p>
