<p>查询最大报单数量请求，对应响应OnRspQryMaxOrderVolume。</p>
<p>虽然ReqQryMaxOrderVolume可以查询可开，但是交易核心在计算的时候是没有算手续费的，所以不完全准，计算逻辑是按照昨结算价计算的可开；如果需要精确结果的，建议自行计算。另外，可平的查询是已经排除了冻结持仓的。</p>
<span class="anchor" id="a31cfc38-0c69-478f-b805-0a88f5984c0e"></span>
## 1.函数原型
<p>virtual int ReqQryMaxOrderVolume(CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, int nRequestID) = 0;</p>
<span class="anchor" id="2b0051ab-eab4-45e4-a659-cdc7bccbfa4c"></span>
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
<span class="anchor" id="446e3a17-0f3e-4959-89f0-fe167de9685c"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="daceb0bb-6d0b-4ac9-b3ad-a6b9632d4b13"></span>
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
<span class="anchor" id="7ae3ad6e-ad4d-4355-bd4b-0de1f27e30e8"></span>
## 5.FAQ
<p>无</p>
