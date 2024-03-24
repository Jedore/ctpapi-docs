<p>请求查询二级代理商资金校验模式</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSECAGENTCHECKMODE/">OnRspQrySecAgentCheckMode</a></p>
<span class="anchor" id="add790dd-488e-416a-9860-2b02cec734e2"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentCheckMode(CThostFtdcQrySecAgentCheckModeField *pQrySecAgentCheckMode, int nRequestID) = 0;</p>
<span class="anchor" id="69b6eec4-217b-402f-bb2b-87e1221ab257"></span>
## 2.参数
<p>pQrySecAgentCheckMode：查询二级代理商资金校验模式</p>
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
</table>
<p>使用二级代理商操作员管理的投资者进行查询，字段值填写正确时，有查询结果。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="1c274fed-8a2e-4e77-8a19-1d65302db9fb"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="419354bd-f01e-4dde-bcd9-3d35db610b72"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="b969936e-7b0c-4e67-9408-842f333542bc"></span>
## 5.FAQ
<p>无</p>
