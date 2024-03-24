<p>请求查询二级代理商资金校验模式</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSECAGENTCHECKMODE/">OnRspQrySecAgentCheckMode</a></p>
<span class="anchor" id="903f1aad-e38d-458e-bce9-ff1de3ba7671"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentCheckMode(CThostFtdcQrySecAgentCheckModeField *pQrySecAgentCheckMode, int nRequestID) = 0;</p>
<span class="anchor" id="80fc3e92-8c0d-4842-b523-19ba313963d4"></span>
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
<span class="anchor" id="69ea360e-bfb4-4139-a6ac-772cc1fa09d5"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c39406d4-9121-4741-a84c-ecfd31f34b8a"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="f2dc7f14-28b1-4f2a-bb9c-c7b9c2370cdb"></span>
## 5.FAQ
<p>无</p>
