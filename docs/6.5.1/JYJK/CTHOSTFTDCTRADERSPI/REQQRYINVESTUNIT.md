<p>请求查询投资单元</p>
<p>响应: OnRspQryInvestUnit</p>
<span class="anchor" id="7f2c00d4-7136-4ede-8476-192ec3e9f84d"></span>
## 1.函数原型
<p>virtual int ReqQryInvestUnit(CThostFtdcQryInvestUnitField *pQryInvestUnit, int nRequestID) = 0;</p>
<span class="anchor" id="072a2ea9-e634-435d-8e7d-c48f6e021176"></span>
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
<p>字段填写正确是，返回“无此功能”</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="8db0b4ab-442f-403e-b401-570d67a9e89d"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ec3ff3e8-3ccb-4e2b-b36f-fb8fca51353a"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="c2ce7746-321c-42cb-8249-6131a1d1b8b9"></span>
## 5.FAQ
<p>无</p>
