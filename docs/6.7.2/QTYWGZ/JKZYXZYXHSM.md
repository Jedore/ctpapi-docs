<span class="anchor" id="41d9b8a9-8760-47b1-82dc-1af879e86626"></span>
## 1. 报单
<span class="anchor" id="2a39b250-1276-45ba-a5f8-77f112533136"></span>
### 1.1. FrontID + SessionID + OrderRef  
<p>当报单报入CTP后，这组序号可以唯一定位一笔报单。可以用于跟踪报单回报的整个生命周期，但无法跟踪成交回报，因为成交回报里没有这组序号。  </p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配，即对于同一笔报单，清流重启前后的这组序号会不一致，使用上需注意。</p>
<span class="anchor" id="b5cfe3b8-b860-4a2e-a285-541e33bcf6b6"></span>
### 1.2. ExchangeID + TraderID + OrderLocalID  
<p>当报单被CTP接受后，系统会分配OrderLocalID并发往交易所，这组序号可以用于跟踪此后报单的生命周期，包括报单回报和成交回报。</p>
<p>当报单被CTP拒绝后，不会分配OrderLocalID，此时仍要使用第1组序号跟踪报单。</p>
<p>注意：CTP清流重启后报单回报中的该组序号保持不变。</p>
<span class="anchor" id="e2e07860-8d7e-44af-b552-62583a145060"></span>
### 1.3. ExchangeID + OrderSysID  
<p>当报单被交易所接受后，交易所系统会分配OrderSysID并给CTP推送报单回报，这组序号可以用于跟踪此后报单的生命周期，包括报单回报和成交回报。</p>
<p>当报单被交易所拒绝后，交易所不会分配OrderSysID，此时仍要使用第1和第2组序号跟踪报单。</p>
<p>注意：CTP清流重启后报单回报中的该组序号保持不变。</p>
<span class="anchor" id="625a6e79-4080-49e9-acd8-1951b4d02876"></span>
### 1.4. RequestID
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a>中的RequestID与<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的相对应，可以用于跟踪报单回报的整个生命周期，但无法跟踪成交回报，因为成交回报里没有这个字段。</p>
<p>注意：CTP清流重启后该序号置零。</p>
<span class="anchor" id="5fb27f33-a9bf-4d01-af07-6e84168215bf"></span>
### 1.5. RelativeOrderSysID
<p>用于关联条件报单和触发后的报单回报。当报入条件单后，会生成OrderSysID=TJBD_XX的报单，此时状态为未触发；当行情满足条件并触发条件单后，会生成一笔新的报单，其RelativeOrderSysID=TJBD_XX。</p>
<p>注意：CTP清流重启后RelativeOrderSysID会清空，无法再关联条件单。</p>
<span class="anchor" id="f7d573e6-574f-4d6a-8d34-e4a57ffa040b"></span>
## 2. 报价
<span class="anchor" id="d945b539-fdd6-494b-86df-dbedc1ad6d19"></span>
### 2.1. FrontID + SessionID + QuoteRef
<p>当报价报入CTP后，这组序号可以唯一定位一笔报价。可以用于跟踪报价回报的整个生命周期，但无法跟踪报价衍生单，因为报价衍生单回报（<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>和<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a>）里没有这组序号。  </p>
<p>注意：CTP清流重启后报价中的该组序号会重新分配，即对于同一笔报价，清流重启前后的这组序号会不一致，使用上需注意。</p>
<span class="anchor" id="e2c783b8-151e-42c6-8e87-4f432db4824c"></span>
### 2.2. FrontID + SessionID + AskOrderRef/BidOrderRef  
<p>当报价报入CTP后，可以通过报价回报中的这组序号跟踪报价衍生单，AskOrderRef对应报价衍生卖单的OrderRef，BidOrderRef对应报价衍生买单的OrderRef。规则同上面报单接口的序号1。</p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配。</p>
<span class="anchor" id="60a98841-a8c5-4a27-b6c8-4b409d88ffc9"></span>
### 2.3. ExchangeID + TraderID + QuoteLocalID
<p>当报价被CTP接受后，系统会分配QuoteLocalID并发往交易所，这组序号可以用于跟踪此后报价的生命周期，但无法跟踪报价衍生单，因为报价衍生单回报里没有这组序号。衍生单的序号规则同上面报价接口序号2。</p>
<p>当报价被CTP拒绝后，不会分配QuoteLocalID，此时仍要使用第1组序号跟踪报价。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="24a5317f-2561-4083-b21d-edc71120df49"></span>
### 2.4. ExchangeID + QuoteSysID
<p>当报价被交易所接受后，交易所系统会分配QuoteSysID并给CTP推送报价回报，这组序号可以用于跟踪此后报价的生命周期，但无法跟踪报价衍生单，因为报价衍生单回报里没有这组序号。</p>
<p>当报价被交易所拒绝后，交易所不会分配QuoteSysID，此时仍要使用第1和第3组序号跟踪报价。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="05e49a25-665b-4dde-91a0-88c4d1100cab"></span>
### 2.5. ExchangeID + AskOrderSysID/BidOrderSysID
<p>当报价被交易所接受后，上期所、能源中心、中金所可以通过报价回报中的这组序号跟踪报价衍生单，AskOrderSysID对应报价衍生卖单的OrderSysID，BidOrderSysID对应报价衍生买单的OrderSysID。衍生单的序号规则同上面报单接口。</p>
<p>大商所和郑商所的报价回报中，AskOrderSysID和BidOrderSysID为空。</p>
<p>大商所报价回报中QuoteSysID对应买衍生单的的OrderSysID，QuoteSysID+1的值对应卖衍生单的OrderSysID，比如报价回报中QuoteSysID为110，那么衍生单的OrderSysID分别是110和111。</p>
<p>郑商所报价回报中QuoteSysID的前缀加上'a'对应卖衍生单的OrderSysID，QuoteSysID的前缀加上'b'对应买衍生单的OrderSysID，比如报价回报的QuoteSysID为110，那么衍生单的OrderSysID分别是a110、b110。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="d2dc1d08-eac6-4f54-98a5-64a4775d64b1"></span>
### 2.6. RequestID
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQQUOTEINSERT/">ReqQuoteInsert</a>中的RequestID与<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNQUOTE/">OnRtnQuote</a>和<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的相对应，用于跟踪报价回报和报价衍生单回报的整个生命周期。例如<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQQUOTEINSERT/">ReqQuoteInsert</a>中RequestID=888，则<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNQUOTE/">OnRtnQuote</a>的RequestID=888，买衍生单的<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的RequestID=888，卖衍生单<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的RequestID=888。</p>
<p>注意：CTP清流重启后该序号置零。</p>
<span class="anchor" id="2da45365-2e82-441a-a6ec-40c605d3d24e"></span>
## 3. 询价
<span class="anchor" id="91553517-ac79-495e-ae1d-e6ccdf67ed53"></span>
### 3.1. ForQuoteRef
<p>当询价请求报入CTP后，该字段用来唯一定位一笔询价。</p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配。</p>
<span class="anchor" id="6676f570-5a8b-469c-a418-f17075ace807"></span>
### 3.2. ForQuoteSysID
<p>当询价被交易所接受后，交易所系统分配ForQuoteSysID，可以用于跟踪此后询价的的生命周期。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="5d7e4ced-5a2b-4f52-9882-be0ac297eacf"></span>
## 4. 行权
<span class="anchor" id="a66c924b-11a6-4bbd-8227-e8467d087b53"></span>
### 4.1. FrontID + SessionID + ExecOrderRef
<p>当行权请求报入CTP后，该组序号用来唯一定位一笔行权。</p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配。</p>
<span class="anchor" id="3917be98-5cfb-4d4f-9e85-76c44284e945"></span>
### 4.2. ExchangeID + TraderID + ExecOrderLocalID
<p>当行权被CTP接受后，可以通过行权回报中的这组序号跟踪此后行权的生命周期。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="d6e9e05d-7433-4a9b-9f93-894d272bb48a"></span>
### 4.3. ExchangeID + ExecOrderSysID
<p>当行权被交易所接受后，可以通过行权回报中的这组序号跟踪此后行权的生命周期。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="763315d9-9b0b-49df-976f-012c9fe120f4"></span>
## 5. 自对冲
<span class="anchor" id="eb46c5a2-02cb-435d-a8e5-bf0b3c582fef"></span>
### 5.1. FrontID + SessionID + OptionSelfCloseRef
<p>当自对冲报入CTP后，这组序号可以唯一定位一笔自对冲。可以用于跟踪自对冲回报的整个生命周期。  </p>
<p>注意：CTP清流重启后自对冲中的该组序号会重新分配，即对于同一笔自对冲，清流重启前后的这组序号会不一致，使用上需注意。</p>
<span class="anchor" id="79d1455e-71ff-4fa2-ad81-0d0cd738fb15"></span>
### 5.2. ExchangeID + TraderID + OptionSelfCloseLocalID
<p>当自对冲被CTP接受后，系统会分配OptionSelfCloseLocalID并发往交易所，这组序号可以用于跟踪此后自对冲的生命周期。</p>
<p>当自对冲被CTP拒绝后，不会分配OptionSelfCloseLocalID，此时仍要使用第1组序号跟踪自对冲。</p>
<p>注意：CTP清流重启后自对冲回报中的该组序号保持不变。</p>
<span class="anchor" id="d5eccbc4-d34b-42b0-a487-a5f53b915f57"></span>
### 5.3. ExchangeID + OptionSelfCloseSysID
<p>当自对冲被交易所接受后，交易所系统会分配OptionSelfCloseSysID并给CTP推送自对冲回报，这组序号可以用于跟踪此后自对冲的生命周期。</p>
<p>当自对冲被交易所拒绝后，交易所不会分配OptionSelfCloseSysID，此时仍要使用第1和第2组序号跟踪自对冲。</p>
<p>注意：CTP清流重启后自对冲回报中的该组序号保持不变。</p>
<blockquote>
<p>大商所不适用此序号，因为大商所不分配OptionSelfCloseSysID值。</p>
</blockquote>
<span class="anchor" id="9af78b8f-ce7d-495c-98d8-4435e81d4235"></span>
### 5.4. RequestID
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEINSERT/">ReqOptionSelfCloseInsert</a>中的RequestID与<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNOPTIONSELFCLOSE/">OnRtnOptionSelfClose</a>中的相对应，用于跟踪自对冲回报的整个生命周期。</p>
<p>注意：CTP清流重启后该序号置零。</p>
