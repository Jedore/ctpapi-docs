<p>请求查询交易编码</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYTRADINGCODE/">OnRspQryTradingCode</a></p>
<span class="anchor" id="57f6e027-4fce-4583-b501-205fcf88963c"></span>
## 1.函数原型
<p>virtual int ReqQryTradingCode(CThostFtdcQryTradingCodeField *pQryTradingCode, int nRequestID) = 0;</p>
<span class="anchor" id="b1cf52c5-8a1c-411a-b084-7c95b29ccddf"></span>
## 2.参数
<p>pQryTradingCode：查询交易编码</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcClientIDType</td>
<td style="TEXT-ALIGN: left;">ClientID</td>
<td style="TEXT-ALIGN: left;">客户代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestUnitIDType</td>
<td style="TEXT-ALIGN: left;">InvestUnitID</td>
<td style="TEXT-ALIGN: left;">投资单元代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcClientIDTypeType</td>
<td style="TEXT-ALIGN: left;">ClientIDType</td>
<td style="TEXT-ALIGN: left;">交易编码类型</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="90f2001b-9eea-4bf6-83f0-ef12fe956c09"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="a10585b6-923a-45ed-9fef-155928e36afc"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="fb09505e-7ddc-4f4c-a11e-845c8eb6f70f"></span>
## 5.FAQ
<p>无</p>
