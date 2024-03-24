<p>请求投资者SPBM套餐选择查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMINVESTORPORTFDEF/">OnRspQrySPBMInvestorPortfDef</a></p>
<span class="anchor" id="e4674827-2f54-4275-bdbf-e446a4e9b401"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMInvestorPortfDef(CThostFtdcQrySPBMInvestorPortfDefField *pQrySPBMInvestorPortfDef, int nRequestID) = 0;</p>
<span class="anchor" id="f260a219-86ef-4f07-ac03-bd3eadf7ee32"></span>
## 2.参数
<p>pQrySPBMInvestorPortfDef：投资者套餐选择查询</p>
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
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="e05e29e3-4c58-470d-b6ee-ac7fe7ab9624"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="cbf18611-54e1-43ee-8cbf-db08be9c519a"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="a33d80aa-2cb7-4145-b3d0-a35f53c63a9e"></span>
## 5.FAQ
<p>无</p>
