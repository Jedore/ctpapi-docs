<p>请求删除预埋撤单，对应响应<a href="../../CTHOSTFTDCTRADERAPI/ONRSPREMOVEPARKEDORDERACTION/">OnRspRemoveParkedOrderAction</a>。该函数用于删除已经报入但未触发的某笔预埋撤单，注意是预埋撤单，而不是预埋报单。删除预埋报单使用<a href="../REQREMOVEPARKEDORDER/">ReqRemoveParkedOrder</a>。</p>
<span class="anchor" id="7ec7b8ac-a3df-4aad-bd9e-d17f1af48de3"></span>
## 1.函数原型
<p>virtual int ReqRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, int nRequestID) = 0;</p>
<span class="anchor" id="8feff68e-f0e5-4245-b666-9b723577b1e2"></span>
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
<span class="anchor" id="0d784ffa-c27c-47c3-8832-ef00c454dec6"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="53e933fa-6e9b-48bb-a1ba-cb705579d041"></span>
## 4.调用示例
<pre><code>CThostFtdcRemoveParkedOrderActionField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.ParkedOrderActionID, "1");  
m_pUserApi-&gt;ReqRemoveParkedOrderAction(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="82491d33-2fd4-4ed1-95fb-fc7969e3f521"></span>
## 5.FAQ
<p>无</p>
