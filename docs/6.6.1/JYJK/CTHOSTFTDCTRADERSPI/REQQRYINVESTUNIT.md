<p>请求查询投资单元，暂不支持此功能</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTUNIT/">OnRspQryInvestUnit</a></p>
<span class="anchor" id="78f4ce9a-ea9e-44c5-8227-e45fa92ec1a4"></span>
## 1.函数原型
<p>virtual int ReqQryInvestUnit(CThostFtdcQryInvestUnitField *pQryInvestUnit, int nRequestID) = 0;</p>
<span class="anchor" id="b774c0c5-e246-4533-901b-4dd71628628b"></span>
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
<span class="anchor" id="46724826-1fc9-4b32-83af-5b852fbda3b1"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ea115644-a3a4-4b50-a6f5-20ac26ff5338"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="b5e97d84-bb48-4a47-88ad-745cda42aae9"></span>
## 5.FAQ
<p>无</p>
