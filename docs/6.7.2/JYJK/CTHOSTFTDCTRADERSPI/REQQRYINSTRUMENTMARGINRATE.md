<p>请求查询合约保证金率，对应响应<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINSTRUMENTMARGINRATE/">OnRspQryInstrumentMarginRate</a>。如果InstrumentID填空，则返回持仓对应的合约保证金率，否则返回相应InstrumentID的保证金率。</p>
<blockquote>
<p>目前无法通过一次查询得到所有合约保证金率，如果要查询所有，则需要通过多次查询得到。</p>
</blockquote>
<span class="anchor" id="87e2912f-d86f-4a03-91fc-8fc34f1f8a28"></span>
## 1.函数原型
<p>virtual int ReqQryInstrumentMarginRate(CThostFtdcQryInstrumentMarginRateField *pQryInstrumentMarginRate, int nRequestID) = 0;</p>
<span class="anchor" id="3846e9ef-b3fc-4eea-ae21-7551886ec714"></span>
## 2.参数
<p>pQryInstrumentMarginRate：查询合约保证金率</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestUnitIDType</td>
<td style="TEXT-ALIGN: left;">InvestUnitID</td>
<td style="TEXT-ALIGN: left;">投资单元代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcHedgeFlagType</td>
<td style="TEXT-ALIGN: left;">HedgeFlag</td>
<td style="TEXT-ALIGN: left;">投机套保标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="b5ce7b3e-479a-4d86-bb87-c271d3ec7ed3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="40cc337b-9a1d-4ed8-8715-5be12b66db70"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInstrumentMarginRateField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
a.HedgeFlag = THOST_FTDC_HF_Speculation;
m_pUserApi-&gt;ReqQryInstrumentMarginRate(&amp;a, 1);
</code></pre>
<span class="anchor" id="ac2fc2db-a57e-4ee3-a48f-d523a3b610af"></span>
## 5.FAQ
<p>无</p>
