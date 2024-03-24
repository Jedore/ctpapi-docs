<p>请求查询合约手续费率，对应响应<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINSTRUMENTCOMMISSIONRATE/">OnRspQryInstrumentCommissionRate</a>。如果InstrumentID填空，则返回持仓对应的合约手续费率。</p>
<blockquote>
<p>目前无法通过一次查询得到所有合约手续费率，如果要查询所有，则需要通过多次查询得到。</p>
</blockquote>
<span class="anchor" id="b44e8f0a-72e3-4f29-8bd8-1b880d1e8c64"></span>
## 1.函数原型
<p>virtual int ReqQryInstrumentCommissionRate(CThostFtdcQryInstrumentCommissionRateField *pQryInstrumentCommissionRate, int nRequestID) = 0;</p>
<span class="anchor" id="6708b4b5-6206-4b58-957a-db389bc9ec8f"></span>
## 2.参数
<p>pQryInstrumentCommissionRate：查询手续费率</p>
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
<p>InstrumentID：返回手续费率对应的合约。</p>
<blockquote>
<p>但是如果在柜台没有设置具体合约的手续费率，则默认会返回产品的手续费率，InstrumentID就为对应产品ID。</p>
</blockquote>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="dc3e3a56-b3a5-4650-bda0-86564186ec5e"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="f45d3351-2183-4190-b4c8-9ffe04baa103"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInstrumentCommissionRateField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
m_pUserApi-&gt;ReqQryInstrumentCommissionRate(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="c1ca4f04-ce18-4051-b015-e937428801d2"></span>
## 5.FAQ
<p>无</p>
