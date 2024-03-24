<p>请求查询期权交易成本，该函数用于查期权保证金，对应响应<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYOPTIONINSTRTRADECOST/">OnRspQryOptionInstrTradeCost</a>。</p>
<blockquote>
<p><code>保证金=max(权利金+FixedMargin,MiniMargin)</code>，用户可根据此公式计算实时保证金。</p>
</blockquote>
<span class="anchor" id="f499c75e-4ebb-4a82-819b-f0075b8080cc"></span>
## 1.函数原型
<p>virtual int ReqQryOptionInstrTradeCost(CThostFtdcQryOptionInstrTradeCostField *pQryOptionInstrTradeCost, int nRequestID) = 0;</p>
<span class="anchor" id="8124ffbc-691c-473c-87fd-d7ee3e2a8111"></span>
## 2.参数
<p>pQryOptionInstrTradeCost：期权交易成本查询</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPriceType</td>
<td style="TEXT-ALIGN: left;">InputPrice</td>
<td style="TEXT-ALIGN: left;">期权合约报价</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPriceType</td>
<td style="TEXT-ALIGN: left;">UnderlyingPrice</td>
<td style="TEXT-ALIGN: left;">标的价格,填0则用昨结算价</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="002e78dd-9d89-43c3-b8c5-bf01a5a13fb3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="d7f4813f-0c31-4587-ba5e-938d5d7fdf86"></span>
## 4.调用示例
<pre><code>CThostFtdcQryOptionInstrTradeCostField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
a.HedgeFlag = THOST_FTDC_HF_Speculation;
a.InputPrice = 300; 
m_pUserApi-&gt;ReqQryOptionInstrTradeCost(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="38055cf7-93ac-47e8-accf-c445ee45275d"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">为什么我用这个接口算出来的保证金跟资金查询得到的保证金占用不一致？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>ReqQryOptionInstrTradeCost计算出的期权保证金跟资金查询里的期权保证金的计算方式不一样。</p>
<p>ReqQryOptionInstrTradeCost只是估计计算，因为其使用的公式（保证金=max(权利金+FixedMargin,MiniMargin)）中的权利金部分在计算时使用的期权价格是InputPrice。</p>
<p>而资金查询里的期权保证金计算公式中的期权价格是使用max算法（max(昨结算，最新价)）得到的。</p>
<p>所以两者存在差别。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
