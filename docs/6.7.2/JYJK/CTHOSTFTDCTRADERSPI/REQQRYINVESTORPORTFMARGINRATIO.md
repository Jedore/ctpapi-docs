<p>请求投资者新型组合保证金系数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPORTFMARGINRATIO/">OnRspQryInvestorPortfMarginRatio</a></p>
<span class="anchor" id="cde77273-a738-4dd6-b077-581347c62550"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorPortfMarginRatio(CThostFtdcQryInvestorPortfMarginRatioField *pQryInvestorPortfMarginRatio, int nRequestID) = 0;</p>
<span class="anchor" id="b9655209-0598-47dc-9b4a-868069305821"></span>
## 2.参数
<p>pQryInvestorPortfMarginRatio：投资者新型组合保证金系数查询</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="c0d80855-b6bd-41f9-9214-49d9e5c62f0f"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="8907ed5a-075d-4e0b-a4fa-e558a9d0ab2b"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="40e39565-40cf-48bc-a346-b53a79b008ba"></span>
## 5.FAQ
<p>无</p>
