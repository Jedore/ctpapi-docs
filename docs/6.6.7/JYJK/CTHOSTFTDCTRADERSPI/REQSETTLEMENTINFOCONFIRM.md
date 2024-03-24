<p>投资者结算结果确认，在开始每日交易前都需要先确认上一日结算单，只需要确认一次。对应响应<a href="../../CTHOSTFTDCTRADERAPI/ONRSPSETTLEMENTINFOCONFIRM/">OnRspSettlementInfoConfirm</a>。</p>
<span class="anchor" id="1995a88a-083e-44ff-8a07-c37355d26655"></span>
## 1.函数原型
<p>virtual int ReqSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, int nRequestID) = 0;</p>
<span class="anchor" id="ca1dd785-5b58-45b2-96b2-1e0d1e64934b"></span>
## 2.参数
<p>pSettlementInfoConfirm：投资者结算结果确认信息</p>
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
<td style="TEXT-ALIGN: left;">ConfirmDate</td>
<td style="TEXT-ALIGN: left;">确认日期</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcTimeType</td>
<td style="TEXT-ALIGN: left;">ConfirmTime</td>
<td style="TEXT-ALIGN: left;">确认时间</td>
<td style="TEXT-ALIGN: left;">否</td>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcSettlementIDType</td>
<td style="TEXT-ALIGN: left;">SettlementID</td>
<td style="TEXT-ALIGN: left;">结算编号</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="ccd2ccf9-3232-4388-a340-25acf5faa6bb"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c77456aa-146a-4c65-b0a8-ee4de4748935"></span>
## 4.调用示例
<pre><code>CThostFtdcSettlementInfoConfirmField Confirm = { 0 };
strcpy_s(Confirm.BrokerID, "9999"); 
strcpy_s(Confirm.InvestorID, "1000001");
m_pUserApi-&gt;ReqSettlementInfoConfirm(&amp;Confirm, nRequestID++);
</code></pre>
<span class="anchor" id="dfb40a6a-7786-46c6-b40c-d2c68c9b85d4"></span>
## 5.FAQ
<p>无</p>
