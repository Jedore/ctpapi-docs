<p>请求查询投资者结算结果，对应响应<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSETTLEMENTINFO/">OnRspQrySettlementInfo</a>。可以查询当天或历史结算单，也可以查询月结算单，但是前提是CTP柜台生成了相应的日或月结算单。</p>
<span class="anchor" id="ed35a56d-796f-47c9-bb20-dc7693dfb327"></span>
## 1.函数原型
<p>virtual int ReqQrySettlementInfo(CThostFtdcQrySettlementInfoField *pQrySettlementInfo, int nRequestID) = 0;</p>
<span class="anchor" id="87297051-4072-4ae5-afb6-4088d93463c9"></span>
## 2.参数
<p>pQrySettlementInfo：查询投资者结算结果</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcDateType</td>
<td style="TEXT-ALIGN: left;">TradingDay</td>
<td style="TEXT-ALIGN: left;">交易日</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcAccountIDType</td>
<td style="TEXT-ALIGN: left;">AccountID</td>
<td style="TEXT-ALIGN: left;">投资者帐号</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCurrencyIDType</td>
<td style="TEXT-ALIGN: left;">CurrencyID</td>
<td style="TEXT-ALIGN: left;">币种代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>TradingDay：查询某一天的结算单，填写格式为“yyyymmdd”；查询某一月的结算单，填写格式为“yyyymm”</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="d4c8e74d-f00d-47aa-8368-4f630c76d032"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="d2e21918-6850-4244-8594-2830eceb6c79"></span>
## 4.调用示例
<pre><code>CThostFtdcQrySettlementInfoField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.TradingDay,“20180101”);
m_pUserApi-&gt;ReqQrySettlementInfo(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="d607939b-8a2b-422f-b546-0d28d104e88f"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">为什么我查不到月结单？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>这有可能是CTP系统里没有生成你的月结算单。CTP的日结算单是需要每天结算的时候业务人员去点击生成的，月结算单也是需要定期生成的。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
