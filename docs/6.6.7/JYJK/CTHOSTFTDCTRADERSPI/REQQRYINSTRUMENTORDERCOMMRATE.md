<span class="anchor" id="3961e128-8f7a-434d-806d-f5d58ab85fad"></span>
## 1.说明
<p>请求查询报单手续费</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINSTRUMENTORDERCOMMRATE/">OnRspQryInstrumentOrderCommRate</a></p>
<span class="anchor" id="da52b135-3529-437b-ac17-4fb8b797d0eb"></span>
## 2.函数原型
<p>virtual int ReqQryInstrumentOrderCommRate(CThostFtdcQryInstrumentOrderCommRateField *pQryInstrumentOrderCommRate, int nRequestID) = 0;</p>
<span class="anchor" id="31508947-782d-4c49-a504-673e5f9f06ac"></span>
## 3.参数
<p>pQryInstrumentOrderCommRate：报单手续费率查询</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="97b866e1-d34d-45a7-be1c-baafc41f2fa8"></span>
## 4.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c7b6df68-828e-44a1-a87e-9a71fd16572e"></span>
## 5.调用示例
<pre><code>CThostFtdcQryInstrumentOrderCommRateField a = { 0 };
strcpy(a.BrokerID, "9999");
strcpy(a.InvestorID, "1000001");
strcpy(a.InstrumentID, "rb1809");
m_pUserApi-&gt;ReqQryInstrumentOrderCommRate(&amp;a, 1);
</code></pre>
<span class="anchor" id="5a4f7193-0b1c-40df-8dd1-25c230966015"></span>
## 6.FAQ
<p>无</p>
