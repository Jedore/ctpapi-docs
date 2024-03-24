<span class="anchor" id="bda2f160-1ee8-4969-87a4-02a111c9b674"></span>
## 1. 报单
<span class="anchor" id="f665e591-b5ac-41b7-8ed8-d8e14511fc9d"></span>
### 1.1. FrontID + SessionID + OrderRef  
<p>当报单报入CTP后，这组序号可以唯一定位一笔报单。可以用于跟踪报单回报的整个生命周期，但无法跟踪成交回报，因为成交回报里没有这组序号。  </p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配，即对于同一笔报单，清流重启前后的这组序号会不一致，使用上需注意。</p>
<span class="anchor" id="234a4185-9bbb-4aa7-88ca-04ad00b4b742"></span>
### 1.2. ExchangeID + TraderID + OrderLocalID  
<p>当报单被CTP接受后，系统会分配OrderLocalID并发往交易所，这组序号可以用于跟踪此后报单的生命周期，包括报单回报和成交回报。</p>
<p>当报单被CTP拒绝后，不会分配OrderLocalID，此时仍要使用第1组序号跟踪报单。</p>
<p>注意：CTP清流重启后报单回报中的该组序号保持不变。</p>
<span class="anchor" id="ee2b20b7-7ed2-4607-9467-0f24f16108e1"></span>
### 1.3. ExchangeID + OrderSysID  
<p>当报单被交易所接受后，交易所系统会分配OrderSysID并给CTP推送报单回报，这组序号可以用于跟踪此后报单的生命周期，包括报单回报和成交回报。</p>
<p>当报单被交易所拒绝后，交易所不会分配OrderSysID，此时仍要使用第1和第2组序号跟踪报单。</p>
<p>注意：CTP清流重启后报单回报中的该组序号保持不变。</p>
<span class="anchor" id="b48beea1-f77d-485c-be2c-da20d5675a1e"></span>
### 1.4. RequestID
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a>中的RequestID与<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的相对应，可以用于跟踪报单回报的整个生命周期，但无法跟踪成交回报，因为成交回报里没有这个字段。</p>
<p>注意：CTP清流重启后该序号置零。</p>
<span class="anchor" id="7d35cb20-ab6a-48bf-a7e3-94ef4bceeefe"></span>
### 1.5. RelativeOrderSysID
<p>用于关联条件报单和触发后的报单回报。当报入条件单后，会生成OrderSysID=TJBD_XX的报单，此时状态为未触发；当行情满足条件并触发条件单后，会生成一笔新的报单，其RelativeOrderSysID=TJBD_XX。</p>
<p>注意：CTP清流重启后RelativeOrderSysID会清空，无法再关联条件单。</p>
<span class="anchor" id="54fd5a66-437b-4988-b29d-dcb23e67e193"></span>
## 2. 报价
<span class="anchor" id="d9edbee9-c050-4245-b941-4a0b23321a4c"></span>
### 2.1. FrontID + SessionID + QuoteRef
<p>当报价报入CTP后，这组序号可以唯一定位一笔报价。可以用于跟踪报价回报的整个生命周期，但无法跟踪报价衍生单，因为报价衍生单回报（<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>和<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a>）里没有这组序号。  </p>
<p>注意：CTP清流重启后报价中的该组序号会重新分配，即对于同一笔报价，清流重启前后的这组序号会不一致，使用上需注意。</p>
<span class="anchor" id="2004ede8-ba29-42e4-bd95-fe1c84a93e89"></span>
### 2.2. FrontID + SessionID + AskOrderRef/BidOrderRef  
<p>当报价报入CTP后，可以通过报价回报中的这组序号跟踪报价衍生单，AskOrderRef对应报价衍生卖单的OrderRef，BidOrderRef对应报价衍生买单的OrderRef。规则同上面报单接口的序号1。</p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配。</p>
<span class="anchor" id="f556c371-0984-4faa-8184-770dcb2f1b6e"></span>
### 2.3. ExchangeID + TraderID + QuoteLocalID
<p>当报价被CTP接受后，系统会分配QuoteLocalID并发往交易所，这组序号可以用于跟踪此后报价的生命周期，但无法跟踪报价衍生单，因为报价衍生单回报里没有这组序号。衍生单的序号规则同上面报价接口序号2。</p>
<p>当报价被CTP拒绝后，不会分配QuoteLocalID，此时仍要使用第1组序号跟踪报价。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="1e6d16f3-7497-4c2f-b744-10a90125133d"></span>
### 2.4. ExchangeID + QuoteSysID
<p>当报价被交易所接受后，交易所系统会分配QuoteSysID并给CTP推送报价回报，这组序号可以用于跟踪此后报价的生命周期，但无法跟踪报价衍生单，因为报价衍生单回报里没有这组序号。</p>
<p>当报价被交易所拒绝后，交易所不会分配QuoteSysID，此时仍要使用第1和第3组序号跟踪报价。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="d145db9a-3349-4316-b346-b9d5e843f5d3"></span>
### 2.5. ExchangeID + AskOrderSysID/BidOrderSysID
<p>当报价被交易所接受后，上期所、能源中心、中金所可以通过报价回报中的这组序号跟踪报价衍生单，AskOrderSysID对应报价衍生卖单的OrderSysID，BidOrderSysID对应报价衍生买单的OrderSysID。衍生单的序号规则同上面报单接口。</p>
<p>大商所和郑商所的报价回报中，AskOrderSysID和BidOrderSysID为空。</p>
<p>大商所报价回报中QuoteSysID对应买衍生单的的OrderSysID，QuoteSysID+1的值对应卖衍生单的OrderSysID，比如报价回报中QuoteSysID为110，那么衍生单的OrderSysID分别是110和111。</p>
<p>郑商所报价回报中QuoteSysID的前缀加上'a'对应卖衍生单的OrderSysID，QuoteSysID的前缀加上'b'对应买衍生单的OrderSysID，比如报价回报的QuoteSysID为110，那么衍生单的OrderSysID分别是a110、b110。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="3a19c2a2-7bd9-4501-a8a4-6ebf7a8cf348"></span>
### 2.6. RequestID
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQQUOTEINSERT/">ReqQuoteInsert</a>中的RequestID与<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNQUOTE/">OnRtnQuote</a>和<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的相对应，用于跟踪报价回报和报价衍生单回报的整个生命周期。例如<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQQUOTEINSERT/">ReqQuoteInsert</a>中RequestID=888，则<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNQUOTE/">OnRtnQuote</a>的RequestID=888，买衍生单的<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的RequestID=888，卖衍生单<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>中的RequestID=888。</p>
<p>注意：CTP清流重启后该序号置零。</p>
<span class="anchor" id="ea59f127-d13d-4b98-af16-438091933ddc"></span>
## 3. 询价
<span class="anchor" id="ee7a7352-e7d4-4338-bd29-3b52cee5dd0c"></span>
### 3.1. ForQuoteRef
<p>当询价请求报入CTP后，该字段用来唯一定位一笔询价。</p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配。</p>
<span class="anchor" id="999eccf5-556e-4186-ab24-53a48b149591"></span>
### 3.2. ForQuoteSysID
<p>当询价被交易所接受后，交易所系统分配ForQuoteSysID，可以用于跟踪此后询价的的生命周期。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="07e63994-0d2f-4bdc-873b-01d6cfa000ab"></span>
## 4. 行权
<span class="anchor" id="eac6937c-8253-41f3-b483-4658a3501f0c"></span>
### 4.1. FrontID + SessionID + ExecOrderRef
<p>当行权请求报入CTP后，该组序号用来唯一定位一笔行权。</p>
<p>注意：CTP清流重启后报单中的该组序号会重新分配。</p>
<span class="anchor" id="31b1e915-d47e-41ee-aeea-cb84c9ac68f0"></span>
### 4.2. ExchangeID + TraderID + ExecOrderLocalID
<p>当行权被CTP接受后，可以通过行权回报中的这组序号跟踪此后行权的生命周期。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="5afa6124-d257-43af-8a96-9364c85eb496"></span>
### 4.3. ExchangeID + ExecOrderSysID
<p>当行权被交易所接受后，可以通过行权回报中的这组序号跟踪此后行权的生命周期。</p>
<p>注意：CTP清流重启后报价回报中的该组序号保持不变。</p>
<span class="anchor" id="f20c7571-927a-4ed2-be0d-c6db1ec0d662"></span>
## 5. 自对冲
<span class="anchor" id="daa1c340-5f55-44f4-8f1b-452a14a5825e"></span>
### 5.1. FrontID + SessionID + OptionSelfCloseRef
<p>当自对冲报入CTP后，这组序号可以唯一定位一笔自对冲。可以用于跟踪自对冲回报的整个生命周期。  </p>
<p>注意：CTP清流重启后自对冲中的该组序号会重新分配，即对于同一笔自对冲，清流重启前后的这组序号会不一致，使用上需注意。</p>
<span class="anchor" id="1f7ff768-7019-4aa8-bdc8-0949c4c70006"></span>
### 5.2. ExchangeID + TraderID + OptionSelfCloseLocalID
<p>当自对冲被CTP接受后，系统会分配OptionSelfCloseLocalID并发往交易所，这组序号可以用于跟踪此后自对冲的生命周期。</p>
<p>当自对冲被CTP拒绝后，不会分配OptionSelfCloseLocalID，此时仍要使用第1组序号跟踪自对冲。</p>
<p>注意：CTP清流重启后自对冲回报中的该组序号保持不变。</p>
<span class="anchor" id="95410ee3-0a2d-45bb-9fd9-219a45c3b811"></span>
### 5.3. ExchangeID + OptionSelfCloseSysID
<p>当自对冲被交易所接受后，交易所系统会分配OptionSelfCloseSysID并给CTP推送自对冲回报，这组序号可以用于跟踪此后自对冲的生命周期。</p>
<p>当自对冲被交易所拒绝后，交易所不会分配OptionSelfCloseSysID，此时仍要使用第1和第2组序号跟踪自对冲。</p>
<p>注意：CTP清流重启后自对冲回报中的该组序号保持不变。</p>
<blockquote>
<p>大商所不适用此序号，因为大商所不分配OptionSelfCloseSysID值。</p>
</blockquote>
<span class="anchor" id="d2868c8e-62ce-4667-a162-5cb441fe6bc6"></span>
### 5.4. RequestID
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEINSERT/">ReqOptionSelfCloseInsert</a>中的RequestID与<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNOPTIONSELFCLOSE/">OnRtnOptionSelfClose</a>中的相对应，用于跟踪自对冲回报的整个生命周期。</p>
<p>注意：CTP清流重启后该序号置零。</p>
