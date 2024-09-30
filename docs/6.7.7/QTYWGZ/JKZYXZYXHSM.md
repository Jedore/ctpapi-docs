<span class="anchor" id="be202e95-7388-4823-bfa7-d2af09bbcf68"></span>
## 1. 报单
<span class="anchor" id="9e969b8b-0b6f-4dbc-a0c3-a4833647e8e1"></span>
### 1.1. FrontID + SessionID + OrderRef  
<p>当报单报入CTP后，这组序号可以唯一定位一笔报单。可以用于跟踪报单回报的整个生命周期，但无法跟踪成交回报，因为成交回报里没有这组序号。  </p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配，即对于同一笔报单，清流重启前后的这组序号会不一致，使用上需注意。</p>
<span class="anchor" id="58bebf63-111a-4cd7-8aae-91a7cabec4b1"></span>
### 1.2. ExchangeID + TraderID + OrderLocalID  
<p>当报单被CTP接受后，系统会分配OrderLocalID并发往交易所，这组序号可以用于跟踪此后报单的生命周期，包括报单回报和成交回报。</p>
<p>当报单被CTP拒绝后，不会分配OrderLocalID，此时仍要使用第1组序号跟踪报单。</p>
<p>注意：CTP清流重启后报单回报中的该组序号保持不变。</p>
<span class="anchor" id="116ebd9b-ec31-4f6e-bfcd-69b73b796231"></span>
### 1.3. ExchangeID + OrderSysID  
<p>当报单被交易所接受后，交易所系统会分配OrderSysID并给CTP推送报单回报，这组序号可以用于跟踪此后报单的生命周期，包括报单回报和成交回报。</p>
<p>当报单被交易所拒绝后，交易所不会分配OrderSysID，此时仍要使用第1和第2组序号跟踪报单。</p>
<p>注意：CTP清流重启后报单回报中的该组序号保持不变。</p>
<span class="anchor" id="a36d8f45-f8b5-485e-bdef-349e38e0b375"></span>
### 1.4. RequestID
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a>中的RequestID与<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的相对应，可以用于跟踪报单回报的整个生命周期，但无法跟踪成交回报，因为成交回报里没有这个字段。</p>
<p>注意：CTP清流重启后该序号置零。</p>
<span class="anchor" id="f2557e53-f182-4b04-8f21-a5a4d575d05b"></span>
### 1.5. RelativeOrderSysID
<p>用于关联条件报单和触发后的报单回报。当报入条件单后，会生成OrderSysID=TJBD_XX的报单，此时状态为未触发；当行情满足条件并触发条件单后，会生成一笔新的报单，其RelativeOrderSysID=TJBD_XX。</p>
<p>注意：CTP清流重启后RelativeOrderSysID会清空，无法再关联条件单。</p>
<span class="anchor" id="dfcec772-1e6f-4341-ba62-d34f2fc0e9c5"></span>
## 2. 报价
<span class="anchor" id="193211cf-fe4b-4bb7-b763-69af8c64da8b"></span>
### 2.1. FrontID + SessionID + QuoteRef
<p>当报价报入CTP后，这组序号可以唯一定位一笔报价。可以用于跟踪报价回报的整个生命周期，但无法跟踪报价衍生单，因为报价衍生单回报（<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>和<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a>）里没有这组序号。  </p>
<p>注意：CTP清流重启后报价中的该组序号会重新分配，即对于同一笔报价，清流重启前后的这组序号会不一致，使用上需注意。</p>
<span class="anchor" id="40cf497e-06fe-4e93-961c-f77eab59d1b3"></span>
### 2.2. FrontID + SessionID + AskOrderRef/BidOrderRef  
<p>当报价报入CTP后，可以通过报价回报中的这组序号跟踪报价衍生单，AskOrderRef对应报价衍生卖单的OrderRef，BidOrderRef对应报价衍生买单的OrderRef。规则同上面报单接口的序号1。</p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配。</p>
<span class="anchor" id="ab441459-07b0-4c37-923f-43fc6ab94018"></span>
### 2.3. ExchangeID + TraderID + QuoteLocalID
<p>当报价被CTP接受后，系统会分配QuoteLocalID并发往交易所，这组序号可以用于跟踪此后报价的生命周期，但无法跟踪报价衍生单，因为报价衍生单回报里没有这组序号。衍生单的序号规则同上面报价接口序号2。</p>
<p>当报价被CTP拒绝后，不会分配QuoteLocalID，此时仍要使用第1组序号跟踪报价。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="10d4e1eb-2a0d-45ae-9ead-b75a3e073e9f"></span>
### 2.4. ExchangeID + QuoteSysID
<p>当报价被交易所接受后，交易所系统会分配QuoteSysID并给CTP推送报价回报，这组序号可以用于跟踪此后报价的生命周期，但无法跟踪报价衍生单，因为报价衍生单回报里没有这组序号。</p>
<p>当报价被交易所拒绝后，交易所不会分配QuoteSysID，此时仍要使用第1和第3组序号跟踪报价。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="e56044f3-4a84-4b9a-93cf-8827c33640a3"></span>
### 2.5. ExchangeID + AskOrderSysID/BidOrderSysID
<p>当报价被交易所接受后，上期所、能源中心、中金所可以通过报价回报中的这组序号跟踪报价衍生单，AskOrderSysID对应报价衍生卖单的OrderSysID，BidOrderSysID对应报价衍生买单的OrderSysID。衍生单的序号规则同上面报单接口。</p>
<p>大商所和郑商所的报价回报中，AskOrderSysID和BidOrderSysID为空。</p>
<p>大商所报价回报中QuoteSysID对应买衍生单的的OrderSysID，QuoteSysID+1的值对应卖衍生单的OrderSysID，比如报价回报中QuoteSysID为110，那么衍生单的OrderSysID分别是110和111。</p>
<p>郑商所报价回报中QuoteSysID的前缀加上'a'对应卖衍生单的OrderSysID，QuoteSysID的前缀加上'b'对应买衍生单的OrderSysID，比如报价回报的QuoteSysID为110，那么衍生单的OrderSysID分别是a110、b110。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="41e208df-46de-4211-b384-31dd461f27c3"></span>
### 2.6. RequestID
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQQUOTEINSERT/">ReqQuoteInsert</a>中的RequestID与<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNQUOTE/">OnRtnQuote</a>和<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的相对应，用于跟踪报价回报和报价衍生单回报的整个生命周期。例如<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQQUOTEINSERT/">ReqQuoteInsert</a>中RequestID=888，则<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNQUOTE/">OnRtnQuote</a>的RequestID=888，买衍生单的<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的RequestID=888，卖衍生单<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的RequestID=888。</p>
<p>注意：CTP清流重启后该序号置零。</p>
<span class="anchor" id="1bef0b72-3dec-4c32-8696-62a2bf6eecaa"></span>
## 3. 询价
<span class="anchor" id="52a5989b-d647-4704-be97-f6bc85204135"></span>
### 3.1. ForQuoteRef
<p>当询价请求报入CTP后，该字段用来唯一定位一笔询价。</p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配。</p>
<span class="anchor" id="1cfd89d9-bc0e-448e-a005-ebd24a521616"></span>
### 3.2. ForQuoteSysID
<p>当询价被交易所接受后，交易所系统分配ForQuoteSysID，可以用于跟踪此后询价的的生命周期。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="afe58393-87ee-4438-a8a1-5acc75f8df16"></span>
## 4. 行权
<span class="anchor" id="602d0ac7-beba-4119-9d11-32e99e7a8b16"></span>
### 4.1. FrontID + SessionID + ExecOrderRef
<p>当行权请求报入CTP后，该组序号用来唯一定位一笔行权。</p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配。</p>
<span class="anchor" id="8722390c-c61b-44f5-b8d0-7f8c7cc4493c"></span>
### 4.2. ExchangeID + TraderID + ExecOrderLocalID
<p>当行权被CTP接受后，可以通过行权回报中的这组序号跟踪此后行权的生命周期。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="71a4ab1c-c5a5-4cb7-bcf2-dc762687d33f"></span>
### 4.3. ExchangeID + ExecOrderSysID
<p>当行权被交易所接受后，可以通过行权回报中的这组序号跟踪此后行权的生命周期。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="cb4f678e-fd1e-4b62-a15c-8753ddb1a241"></span>
## 5. 自对冲
<span class="anchor" id="c44c6ca8-479f-4aa9-93f4-7fa751e6877b"></span>
### 5.1. FrontID + SessionID + OptionSelfCloseRef
<p>当自对冲报入CTP后，这组序号可以唯一定位一笔自对冲。可以用于跟踪自对冲回报的整个生命周期。  </p>
<p>注意：CTP清流重启后自对冲中的该组序号会重新分配，即对于同一笔自对冲，清流重启前后的这组序号会不一致，使用上需注意。</p>
<span class="anchor" id="62b8a521-724e-428f-8da6-b6e62d447b2b"></span>
### 5.2. ExchangeID + TraderID + OptionSelfCloseLocalID
<p>当自对冲被CTP接受后，系统会分配OptionSelfCloseLocalID并发往交易所，这组序号可以用于跟踪此后自对冲的生命周期。</p>
<p>当自对冲被CTP拒绝后，不会分配OptionSelfCloseLocalID，此时仍要使用第1组序号跟踪自对冲。</p>
<p>注意：CTP清流重启后自对冲回报中的该组序号保持不变。</p>
<span class="anchor" id="7eae98c3-2380-464d-90de-797aa8d652fe"></span>
### 5.3. ExchangeID + OptionSelfCloseSysID
<p>当自对冲被交易所接受后，交易所系统会分配OptionSelfCloseSysID并给CTP推送自对冲回报，这组序号可以用于跟踪此后自对冲的生命周期。</p>
<p>当自对冲被交易所拒绝后，交易所不会分配OptionSelfCloseSysID，此时仍要使用第1和第2组序号跟踪自对冲。</p>
<p>注意：CTP清流重启后自对冲回报中的该组序号保持不变。</p>
<blockquote>
<p>大商所不适用此序号，因为大商所不分配OptionSelfCloseSysID值。</p>
</blockquote>
<span class="anchor" id="b57ba545-7869-4808-b067-7c510f677667"></span>
### 5.4. RequestID
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEINSERT/">ReqOptionSelfCloseInsert</a>中的RequestID与<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNOPTIONSELFCLOSE/">OnRtnOptionSelfClose</a>中的相对应，用于跟踪自对冲回报的整个生命周期。</p>
<p>注意：CTP清流重启后该序号置零。</p>
