<p>请求查询二级代理商资金校验模式</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSECAGENTCHECKMODE/">OnRspQrySecAgentCheckMode</a></p>
<span class="anchor" id="13c5af38-6007-4f42-8ed9-6d131fd48173"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentCheckMode(CThostFtdcQrySecAgentCheckModeField *pQrySecAgentCheckMode, int nRequestID) = 0;</p>
<span class="anchor" id="46362bc6-e033-4637-88cf-894e90a56bb6"></span>
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
<span class="anchor" id="10145582-db06-4b4f-982d-d21ea5d32b31"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="d1db86ae-8061-4667-8150-112727ba7e57"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="8588b070-ddb8-4352-bcf1-0a40f1ecbe6b"></span>
## 5.FAQ
<p>无</p>
