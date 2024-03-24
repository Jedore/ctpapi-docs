<p>请求删除预埋撤单，对应响应<a href="../../CTHOSTFTDCTRADERAPI/ONRSPREMOVEPARKEDORDERACTION/">OnRspRemoveParkedOrderAction</a>。该函数用于删除已经报入但未触发的某笔预埋撤单，注意是预埋撤单，而不是预埋报单。删除预埋报单使用<a href="../REQREMOVEPARKEDORDER/">ReqRemoveParkedOrder</a>。</p>
<span class="anchor" id="76dde7c0-263d-40a9-b3a8-5b0517a82f40"></span>
## 1.函数原型
<p>virtual int ReqRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, int nRequestID) = 0;</p>
<span class="anchor" id="7d46c489-17ad-4bd5-a54a-bf51735ddb7c"></span>
## 2.参数
<p>pRemoveParkedOrderAction：删除预埋撤单</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">值</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcParkedOrderActionIDType</td>
<td style="TEXT-ALIGN: left;">ParkedOrderActionID</td>
<td style="TEXT-ALIGN: left;">预埋撤单单编号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestUnitIDType</td>
<td style="TEXT-ALIGN: left;">InvestUnitID</td>
<td style="TEXT-ALIGN: left;">投资单元代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
</table>
<p>ParkedOrderActionID：对应的要删除的预埋撤单编号</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="76b4fb31-c484-44ee-9ca8-d2acb1fe2f67"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="5a719f24-d086-4365-8bba-bdb476684045"></span>
## 4.调用示例
<pre><code>CThostFtdcRemoveParkedOrderActionField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.ParkedOrderActionID, "1");  
m_pUserApi-&gt;ReqRemoveParkedOrderAction(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="b683dc9c-c1a5-4c32-b29b-405c860eab33"></span>
## 5.FAQ
<p>无</p>
