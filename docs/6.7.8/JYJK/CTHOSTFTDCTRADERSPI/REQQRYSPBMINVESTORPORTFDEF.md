<p>请求投资者SPBM套餐选择查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMINVESTORPORTFDEF/">OnRspQrySPBMInvestorPortfDef</a></p>
<span class="anchor" id="8988659e-ec07-45ae-991f-e45927d3289b"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMInvestorPortfDef(CThostFtdcQrySPBMInvestorPortfDefField *pQrySPBMInvestorPortfDef, int nRequestID) = 0;</p>
<span class="anchor" id="cb1f5b76-e1c8-4309-946a-a7d9fae55870"></span>
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
<span class="anchor" id="5d735221-f8c7-4451-baf8-6a6089ce787f"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="4cc58349-0926-44af-9e9b-b1069c72a7d2"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="48fd4a8d-fcc0-4d0d-9ca2-f02132266fc4"></span>
## 5.FAQ
<p>无</p>
