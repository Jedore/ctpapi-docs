<p>请求查询投资者持仓，对应响应<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITION/">OnRspQryInvestorPosition</a>。CTP系统将持仓明细记录按合约，持仓方向，开仓日期（仅针对上期所和能源所，区分昨仓、今仓）进行汇总。</p>
<span class="anchor" id="5f85d176-8c08-4e28-9e5d-c662f9dbdfda"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorPosition(CThostFtdcQryInvestorPositionField *pQryInvestorPosition, int nRequestID) = 0;</p>
<span class="anchor" id="f7bb950c-fb16-4978-ae7b-fb9086624ec1"></span>
## 2.参数
<p>pQryInvestorPosition：查询投资者持仓</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="c42bbf7c-0ab4-4556-9f05-d124e67746bf"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="87840c2b-95cb-4b9b-987d-a324563ccc95"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInvestorPositionField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");//不填写合约则返回所有持仓
m_pUserApi-&gt;ReqQryInvestorPosition(&amp;a, 1);
</code></pre>
<span class="anchor" id="704672b3-ba0b-4163-ad60-86cbc295ac35"></span>
## 5.FAQ
<p>无</p>
