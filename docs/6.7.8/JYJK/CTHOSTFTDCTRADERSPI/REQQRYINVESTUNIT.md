<p>请求查询投资单元，暂不支持此功能</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTUNIT/">OnRspQryInvestUnit</a></p>
<span class="anchor" id="916ef361-e035-478a-b740-4f8bbec734b6"></span>
## 1.函数原型
<p>virtual int ReqQryInvestUnit(CThostFtdcQryInvestUnitField *pQryInvestUnit, int nRequestID) = 0;</p>
<span class="anchor" id="2fa6dc13-9faf-464e-bf07-8b13248cc4b7"></span>
## 2.参数
<p>pQryInvestUnit：查询投资单元</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestUnitIDType</td>
<td style="TEXT-ALIGN: left;">InvestUnitID</td>
<td style="TEXT-ALIGN: left;">投资单元代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="e226e78d-b95f-4e7c-943a-5fc1d684973f"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="7683ad20-a6f7-49a3-9901-6b2260034d87"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="cfbf0b27-2779-48d2-b9c7-e6c44cd7ceff"></span>
## 5.FAQ
<p>无</p>
