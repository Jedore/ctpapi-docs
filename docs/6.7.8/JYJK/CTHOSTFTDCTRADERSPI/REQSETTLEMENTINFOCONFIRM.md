<p>投资者结算结果确认，在开始每日交易前都需要先确认上一日结算单，只需要确认一次。对应响应<a href="../../CTHOSTFTDCTRADERAPI/ONRSPSETTLEMENTINFOCONFIRM/">OnRspSettlementInfoConfirm</a>。</p>
<span class="anchor" id="a37296ea-a463-4843-b2f5-3852f1d1c2f7"></span>
## 1.函数原型
<p>virtual int ReqSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, int nRequestID) = 0;</p>
<span class="anchor" id="de991934-b913-403c-b5c9-73befc448f77"></span>
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
<span class="anchor" id="dcdbe12d-ecc1-4eec-87de-463679a7d146"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="4640cb07-6eb3-4bd1-a3df-a1cea0b99cf9"></span>
## 4.调用示例
<pre><code>CThostFtdcSettlementInfoConfirmField Confirm = { 0 };
strcpy_s(Confirm.BrokerID, "9999"); 
strcpy_s(Confirm.InvestorID, "1000001");
m_pUserApi-&gt;ReqSettlementInfoConfirm(&amp;Confirm, nRequestID++);
</code></pre>
<span class="anchor" id="d6556628-34e8-44ec-82af-769d4b29a9a4"></span>
## 5.FAQ
<p>无</p>
