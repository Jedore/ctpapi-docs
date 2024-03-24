<p>请求查询银期签约关系</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYACCOUNTREGISTER/">OnRspQryAccountregister</a></p>
<span class="anchor" id="6e8dbfd8-5fd7-45cc-8e3a-8a5af05a1ff2"></span>
## 1.函数原型
<p>virtual int ReqQryAccountregister(CThostFtdcQryAccountregisterField *pQryAccountregister, int nRequestID) = 0;</p>
<span class="anchor" id="4f27bbed-013e-41b6-a517-647abb07ee56"></span>
## 2.参数
<p>pQryAccountregister：请求查询银期签约关系</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcAccountIDType</td>
<td style="TEXT-ALIGN: left;">AccountID</td>
<td style="TEXT-ALIGN: left;">投资者帐号</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBankIDType</td>
<td style="TEXT-ALIGN: left;">BankID</td>
<td style="TEXT-ALIGN: left;">银行代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBankBrchIDType</td>
<td style="TEXT-ALIGN: left;">BankBranchID</td>
<td style="TEXT-ALIGN: left;">银行分支机构代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCurrencyIDType</td>
<td style="TEXT-ALIGN: left;">CurrencyID</td>
<td style="TEXT-ALIGN: left;">币种代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="56c58a23-502b-435c-9582-e7555a6a8a0d"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1e80e76d-a96c-4105-a829-a2a542956d6b"></span>
## 4.调用示例
<pre><code>CThostFtdcQryAccountregisterField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.AccountID, "1000001");
strcpy_s(a.BankID, "1");
strcpy_s(a.CurrencyID, "CNY");
m_pUserApi-&gt;ReqQryAccountregister(&amp;a, 1);
</code></pre>
<span class="anchor" id="a1af256a-d0d0-498b-9c89-72b80a1864d7"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">查询无结果是什么原因？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>只有和银行签约成功后，并且银行的签约信息返回CTP柜台后才能查询到信息。对应柜台菜单【银期转账账户信息查询】</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
