<p>请求查询期权合约手续费</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYOPTIONINSTRCOMMRATE/">OnRspQryOptionInstrCommRate</a></p>
<span class="anchor" id="f0a864aa-9c67-4a3f-947d-15681e902779"></span>
## 1.函数原型
<p>virtual int ReqQryOptionInstrCommRate(CThostFtdcQryOptionInstrCommRateField *pQryOptionInstrCommRate, int nRequestID) = 0;</p>
<span class="anchor" id="e41a4ba7-e7cc-4e45-8bfa-9b10ab47c6ed"></span>
## 2.参数
<p>pQryOptionInstrCommRate：期权手续费率查询</p>
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
<span class="anchor" id="5675d27c-4194-4f72-8eb2-9ba1dd15be95"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="759bdb4d-0bf5-4985-aaa4-ff272aec9e69"></span>
## 4.调用示例
<p><span alt="" id="anchor-id-02"></span> </p>
<pre><code>CThostFtdcQryOptionInstrCommRateField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "ag2311C1200");
m_pUserApi-&gt;ReqQryOptionInstrCommRate(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="c4c6b7a8-d188-4f6d-b25f-cee6e9649df2"></span>
## 5.FAQ
<p><span alt="" id="anchor-id-01"></span> </p>
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">合约填空，是否能查询所有期权合约手续费率？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>不能，填空只能返回持仓的期权合约手续费率。查询所有期权合约需要一个个请求查询。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
