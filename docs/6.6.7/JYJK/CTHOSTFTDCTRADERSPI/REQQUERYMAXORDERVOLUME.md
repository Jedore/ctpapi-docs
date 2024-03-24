<p>查询最大报单数量请求，对应响应<a href="../../CTHOSTFTDCTRADERAPI/SM/">OnRspQryMaxOrderVolume</a>。</p>
<p>虽然ReqQryMaxOrderVolume可以查询可开，但是交易核心在计算的时候是没有算手续费的，所以不完全准，计算逻辑是按照昨结算价计算的可开；如果需要精确结果的，建议自行计算。另外，可平的查询是已经排除了冻结持仓的。</p>
<span class="anchor" id="065605dc-98b6-4ca8-bc0b-81322e90c72a"></span>
## 1.函数原型
<p>virtual int ReqQryMaxOrderVolume(CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, int nRequestID) = 0;</p>
<span class="anchor" id="dee8aa8a-6738-449d-868d-4fbf667ccac4"></span>
## 2.参数
<p>pQryMaxOrderVolume：查询最大报单数量</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcVolumeType</td>
<td style="TEXT-ALIGN: left;">MaxVolume</td>
<td style="TEXT-ALIGN: left;">最大允许报单数量</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcDirectionType</td>
<td style="TEXT-ALIGN: left;">Direction</td>
<td style="TEXT-ALIGN: left;">买卖方向</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOffsetFlagType</td>
<td style="TEXT-ALIGN: left;">OffsetFlag</td>
<td style="TEXT-ALIGN: left;">开平标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
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
<p>MaxVolume：取值结果为，min（可开/可平，限价单最大下单量）；可开根据昨结算价计算得出。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="f3219c1f-304f-4eac-bde3-e2dbbec70af7"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="15e4fd25-feef-4c39-9606-001e0a5d1124"></span>
## 4.调用示例
<pre><code>CThostFtdcQryMaxOrderVolumeField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
a.Direction = THOST_FTDC_D_Buy;
a.OffsetFlag = THOST_FTDC_OF_Open;
a.HedgeFlag = THOST_FTDC_HF_Speculation;
a.MaxVolume = 1;
m_pUserApi-&gt;ReqQryMaxOrderVolume(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="5b406b69-eda0-4dcf-9f05-bfff87e97e7c"></span>
## 5.FAQ
<p>无</p>
