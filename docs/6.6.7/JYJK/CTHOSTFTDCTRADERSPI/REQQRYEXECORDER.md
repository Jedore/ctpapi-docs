<p>请求查询执行宣告</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYEXECORDER/">OnRspQryExecOrder</a></p>
<span class="anchor" id="075a0f4d-5d57-4544-a625-103af0676f49"></span>
## 1.函数原型
<p>virtual int ReqQryExecOrder(CThostFtdcQryExecOrderField *pQryExecOrder, int nRequestID) = 0;</p>
<span class="anchor" id="d24d9e85-0761-40c0-8354-2b772fe39801"></span>
## 2.参数
<p>pQryExecOrder：执行宣告查询</p>
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
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExecOrderSysIDType</td>
<td style="TEXT-ALIGN: left;">ExecOrderSysID</td>
<td style="TEXT-ALIGN: left;">报单编号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcTimeType</td>
<td style="TEXT-ALIGN: left;">InsertTimeStart</td>
<td style="TEXT-ALIGN: left;">开始时间</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcTimeType</td>
<td style="TEXT-ALIGN: left;">InsertTimeEnd</td>
<td style="TEXT-ALIGN: left;">结束时间</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="5e173c68-9157-4ba8-87a0-93630c51d668"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="de56d56a-dbc6-4a87-b2af-965f9a5bcdc1"></span>
## 4.调用示例
<pre><code>CThostFtdcQryExecOrderField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
strcpy_s(a.ExchangeID, "SHFE");
m_pUserApi-&gt;ReqQryExecOrder(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="8390a241-ad43-45d3-b4f9-15c016e75f26"></span>
## 5.FAQ
<p>无</p>
