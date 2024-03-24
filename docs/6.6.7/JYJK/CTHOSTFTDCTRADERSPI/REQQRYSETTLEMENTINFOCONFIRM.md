<p>请求查询结算信息确认</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSETTLEMENTINFOCONFIRM/">OnRspQrySettlementInfoConfirm</a></p>
<span class="anchor" id="9a7ad877-0aa7-4758-bb7c-d5c6c3c39196"></span>
## 1.函数原型
<p>virtual int ReqQrySettlementInfoConfirm(CThostFtdcQrySettlementInfoConfirmField *pQrySettlementInfoConfirm, int nRequestID) = 0;</p>
<span class="anchor" id="93f3b8ae-a438-4e36-85b5-0768c9de0b5c"></span>
## 2.参数
<p>pQrySettlementInfoConfirm：查询结算信息确认域</p>
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
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="7b940a98-1557-48e5-b69b-c1081a75bc1f"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="a25c949c-31eb-4826-a096-67dba229d96d"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="b9cf10d7-776f-438f-9bff-adc8269eb960"></span>
## 5.FAQ
<p>无</p>
