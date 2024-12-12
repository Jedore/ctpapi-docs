<p>请求投资者产品RULE保证金查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPRODRULEMARGIN/">OnRspQryInvestorProdRULEMargin</a></p>
<span class="anchor" id="fa28f85d-e851-4378-aa01-adbfc6a8c1aa"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorProdRULEMargin(CThostFtdcQryInvestorProdRULEMarginField *pQryInvestorProdRULEMargin, int nRequestID) = 0;</p>
<span class="anchor" id="4e483df8-69c4-4af0-a27d-87ce923b9b50"></span>
## 2.参数
<p>pQryInvestorProdRULEMargin：投资者产品RULE保证金查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
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
<td style="TEXT-ALIGN: left;">ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">品种代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCommodityGroupIDType</td>
<td style="TEXT-ALIGN: left;">CommodityGroupID</td>
<td style="TEXT-ALIGN: left;">商品群号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="06044aa3-0953-4e46-b5d2-bab7786db35c"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="78766b9e-0f1f-49f8-87f2-985d2c323e95"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="aed611f3-8597-4d7e-98be-1b7c1ce76232"></span>
## 5.FAQ
<p>无</p>
