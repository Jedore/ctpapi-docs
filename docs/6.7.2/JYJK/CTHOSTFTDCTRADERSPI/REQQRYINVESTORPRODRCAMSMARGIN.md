<p>请求投资者品种RCAMS保证金查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPRODRCAMSMARGIN/">OnRspQryInvestorProdRCAMSMargin</a></p>
<span class="anchor" id="1510eb89-86db-4c00-a7e5-faf29e247b0d"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorProdRCAMSMargin(CThostFtdcQryInvestorProdRCAMSMarginField *pQryInvestorProdRCAMSMargin, int nRequestID) = 0;</p>
<span class="anchor" id="388f6a33-7e08-44f0-95b2-49a0a2d64d2f"></span>
## 2.参数
<p>pQryInvestorProdRCAMSMargin：投资者品种RCAMS保证金查询</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">CombProductID</td>
<td style="TEXT-ALIGN: left;">产品组合代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">ProductGroupID</td>
<td style="TEXT-ALIGN: left;">商品群代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="570481a9-6825-4a93-b70c-68c1281a7aac"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="79a631f3-fa37-44f5-ac02-092c7ef1a006"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="cc34933c-0287-44a4-ac75-68002dfc9c01"></span>
## 5.FAQ
<p>无</p>
