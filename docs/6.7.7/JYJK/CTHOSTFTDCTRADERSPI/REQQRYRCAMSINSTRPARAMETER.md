<p>请求RCAMS同合约风险对冲参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSINSTRPARAMETER/">OnRspQryRCAMSInstrParameter</a></p>
<span class="anchor" id="84a30cf4-82f0-4996-b3ca-24272dd8ef0b"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSInstrParameter(CThostFtdcQryRCAMSInstrParameterField *pQryRCAMSInstrParameter, int nRequestID) = 0;</p>
<span class="anchor" id="716ad8ab-80d0-4099-ab6e-e44f2a0698fb"></span>
## 2.参数
<p>pQryRCAMSInstrParameter：RCAMS同合约风险对冲参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="3ce8b544-4002-40b8-ba43-568b86443915"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="3a5845ec-c65a-473b-a2c2-89f706521398"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="b3256bc8-5707-49a0-9ff8-878881b91963"></span>
## 5.FAQ
<p>无</p>
