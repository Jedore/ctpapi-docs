<span class="anchor" id="5ab43257-6358-4cc7-b46d-44319619222f"></span>
## 1. 报单
<span class="anchor" id="2249598e-d4b5-4cd4-8476-63926b13d926"></span>
### 1.1. FrontID + SessionID + OrderRef  
<p>当报单报入CTP后，这组序号可以唯一定位一笔报单。可以用于跟踪报单回报的整个生命周期，但无法跟踪成交回报，因为成交回报里没有这组序号。  </p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配，即对于同一笔报单，清流重启前后的这组序号会不一致，使用上需注意。</p>
<span class="anchor" id="acc35048-6d60-4ae9-b0c7-d1daf2c5270f"></span>
### 1.2. ExchangeID + TraderID + OrderLocalID  
<p>当报单被CTP接受后，系统会分配OrderLocalID并发往交易所，这组序号可以用于跟踪此后报单的生命周期，包括报单回报和成交回报。</p>
<p>当报单被CTP拒绝后，不会分配OrderLocalID，此时仍要使用第1组序号跟踪报单。</p>
<p>注意：CTP清流重启后报单回报中的该组序号保持不变。</p>
<span class="anchor" id="aabf98d3-3d42-4469-89f6-10e25fdb3666"></span>
### 1.3. ExchangeID + OrderSysID  
<p>当报单被交易所接受后，交易所系统会分配OrderSysID并给CTP推送报单回报，这组序号可以用于跟踪此后报单的生命周期，包括报单回报和成交回报。</p>
<p>当报单被交易所拒绝后，交易所不会分配OrderSysID，此时仍要使用第1和第2组序号跟踪报单。</p>
<p>注意：CTP清流重启后报单回报中的该组序号保持不变。</p>
<span class="anchor" id="625da1ee-275a-4804-ab5b-665c64a8f14b"></span>
### 1.4. RequestID
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a>中的RequestID与<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的相对应，可以用于跟踪报单回报的整个生命周期，但无法跟踪成交回报，因为成交回报里没有这个字段。</p>
<p>注意：CTP清流重启后该序号置零。</p>
<span class="anchor" id="8ec1a263-e05a-45fc-b456-dcdd85d77a83"></span>
### 1.5. RelativeOrderSysID
<p>用于关联条件报单和触发后的报单回报。当报入条件单后，会生成OrderSysID=TJBD_XX的报单，此时状态为未触发；当行情满足条件并触发条件单后，会生成一笔新的报单，其RelativeOrderSysID=TJBD_XX。</p>
<p>注意：CTP清流重启后RelativeOrderSysID会清空，无法再关联条件单。</p>
<span class="anchor" id="0e45b9c2-78f6-421a-8970-ba8aecf32a0a"></span>
## 2. 报价
<span class="anchor" id="9e3b7a1f-c33c-4a16-8b15-b28095c1b6c5"></span>
### 2.1. FrontID + SessionID + QuoteRef
<p>当报价报入CTP后，这组序号可以唯一定位一笔报价。可以用于跟踪报价回报的整个生命周期，但无法跟踪报价衍生单，因为报价衍生单回报（<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>和<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a>）里没有这组序号。  </p>
<p>注意：CTP清流重启后报价中的该组序号会重新分配，即对于同一笔报价，清流重启前后的这组序号会不一致，使用上需注意。</p>
<span class="anchor" id="f269eb0b-725d-483f-9f8b-409fc632545d"></span>
### 2.2. FrontID + SessionID + AskOrderRef/BidOrderRef  
<p>当报价报入CTP后，可以通过报价回报中的这组序号跟踪报价衍生单，AskOrderRef对应报价衍生卖单的OrderRef，BidOrderRef对应报价衍生买单的OrderRef。规则同上面报单接口的序号1。</p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配。</p>
<span class="anchor" id="47fa1d50-4a35-4ff5-8102-f26c669a9e4f"></span>
### 2.3. ExchangeID + TraderID + QuoteLocalID
<p>当报价被CTP接受后，系统会分配QuoteLocalID并发往交易所，这组序号可以用于跟踪此后报价的生命周期，但无法跟踪报价衍生单，因为报价衍生单回报里没有这组序号。衍生单的序号规则同上面报价接口序号2。</p>
<p>当报价被CTP拒绝后，不会分配QuoteLocalID，此时仍要使用第1组序号跟踪报价。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="458f7a46-bb91-46fc-94b6-b02d5981604c"></span>
### 2.4. ExchangeID + QuoteSysID
<p>当报价被交易所接受后，交易所系统会分配QuoteSysID并给CTP推送报价回报，这组序号可以用于跟踪此后报价的生命周期，但无法跟踪报价衍生单，因为报价衍生单回报里没有这组序号。</p>
<p>当报价被交易所拒绝后，交易所不会分配QuoteSysID，此时仍要使用第1和第3组序号跟踪报价。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="e7c56354-b4fb-4b66-ae0f-7e8dd3dedf1d"></span>
### 2.5. ExchangeID + AskOrderSysID/BidOrderSysID
<p>当报价被交易所接受后，上期所、能源中心、中金所可以通过报价回报中的这组序号跟踪报价衍生单，AskOrderSysID对应报价衍生卖单的OrderSysID，BidOrderSysID对应报价衍生买单的OrderSysID。衍生单的序号规则同上面报单接口。</p>
<p>大商所和郑商所的报价回报中，AskOrderSysID和BidOrderSysID为空。</p>
<p>大商所报价回报中QuoteSysID对应买衍生单的的OrderSysID，QuoteSysID+1的值对应卖衍生单的OrderSysID，比如报价回报中QuoteSysID为110，那么衍生单的OrderSysID分别是110和111。</p>
<p>郑商所报价回报中QuoteSysID的前缀加上'a'对应卖衍生单的OrderSysID，QuoteSysID的前缀加上'b'对应买衍生单的OrderSysID，比如报价回报的QuoteSysID为110，那么衍生单的OrderSysID分别是a110、b110。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="0c66bb9d-6b8a-417f-a32a-88e3e362ddd9"></span>
### 2.6. RequestID
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQQUOTEINSERT/">ReqQuoteInsert</a>中的RequestID与<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNQUOTE/">OnRtnQuote</a>和<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的相对应，用于跟踪报价回报和报价衍生单回报的整个生命周期。例如<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQQUOTEINSERT/">ReqQuoteInsert</a>中RequestID=888，则<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNQUOTE/">OnRtnQuote</a>的RequestID=888，买衍生单的<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的RequestID=888，卖衍生单<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的RequestID=888。</p>
<p>注意：CTP清流重启后该序号置零。</p>
<span class="anchor" id="bcf6783d-6f8c-494e-b9c0-cae5994395fa"></span>
## 3. 询价
<span class="anchor" id="eff86163-c528-4cf6-91f0-b355fff62f38"></span>
### 3.1. ForQuoteRef
<p>当询价请求报入CTP后，该字段用来唯一定位一笔询价。</p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配。</p>
<span class="anchor" id="77d9e102-0612-4ec3-bdad-84dcd932b726"></span>
### 3.2. ForQuoteSysID
<p>当询价被交易所接受后，交易所系统分配ForQuoteSysID，可以用于跟踪此后询价的的生命周期。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="1722f500-8664-47ab-b09a-8b961c8b47f8"></span>
## 4. 行权
<span class="anchor" id="9c4e2c3d-ffe0-416e-8532-1b2ca88ee3fd"></span>
### 4.1. FrontID + SessionID + ExecOrderRef
<p>当行权请求报入CTP后，该组序号用来唯一定位一笔行权。</p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配。</p>
<span class="anchor" id="a1fa8781-98dc-4bae-a495-ceca20c5c676"></span>
### 4.2. ExchangeID + TraderID + ExecOrderLocalID
<p>当行权被CTP接受后，可以通过行权回报中的这组序号跟踪此后行权的生命周期。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="ebd01172-40d7-462b-b2e3-e629d69a28d4"></span>
### 4.3. ExchangeID + ExecOrderSysID
<p>当行权被交易所接受后，可以通过行权回报中的这组序号跟踪此后行权的生命周期。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="4b6c3636-ecd0-41ab-8ae7-cca595aaf5fa"></span>
## 5. 自对冲
<span class="anchor" id="77dcd630-aa39-4e9c-a4d5-168337b4c20a"></span>
### 5.1. FrontID + SessionID + OptionSelfCloseRef
<p>当自对冲报入CTP后，这组序号可以唯一定位一笔自对冲。可以用于跟踪自对冲回报的整个生命周期。  </p>
<p>注意：CTP清流重启后自对冲中的该组序号会重新分配，即对于同一笔自对冲，清流重启前后的这组序号会不一致，使用上需注意。</p>
<span class="anchor" id="094ecd1c-63af-44c4-bff4-b0d879dd4bec"></span>
### 5.2. ExchangeID + TraderID + OptionSelfCloseLocalID
<p>当自对冲被CTP接受后，系统会分配OptionSelfCloseLocalID并发往交易所，这组序号可以用于跟踪此后自对冲的生命周期。</p>
<p>当自对冲被CTP拒绝后，不会分配OptionSelfCloseLocalID，此时仍要使用第1组序号跟踪自对冲。</p>
<p>注意：CTP清流重启后自对冲回报中的该组序号保持不变。</p>
<span class="anchor" id="2e342787-3ee6-420d-8086-1cb60fe5dd67"></span>
### 5.3. ExchangeID + OptionSelfCloseSysID
<p>当自对冲被交易所接受后，交易所系统会分配OptionSelfCloseSysID并给CTP推送自对冲回报，这组序号可以用于跟踪此后自对冲的生命周期。</p>
<p>当自对冲被交易所拒绝后，交易所不会分配OptionSelfCloseSysID，此时仍要使用第1和第2组序号跟踪自对冲。</p>
<p>注意：CTP清流重启后自对冲回报中的该组序号保持不变。</p>
<blockquote>
<p>大商所不适用此序号，因为大商所不分配OptionSelfCloseSysID值。</p>
</blockquote>
<span class="anchor" id="4352049d-915d-45c7-971b-9501f9556897"></span>
### 5.4. RequestID
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEINSERT/">ReqOptionSelfCloseInsert</a>中的RequestID与<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNOPTIONSELFCLOSE/">OnRtnOptionSelfClose</a>中的相对应，用于跟踪自对冲回报的整个生命周期。</p>
<p>注意：CTP清流重启后该序号置零。</p>
