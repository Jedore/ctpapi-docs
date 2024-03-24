<p>请求查询转帐银行</p>
<p>响应: OnRspQryTransferBank</p>
<span class="anchor" id="ef0d9595-a540-4dcd-868e-6fb21af9ab38"></span>
## 1.函数原型
<p>virtual int ReqQryTransferBank(CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID) = 0;</p>
<span class="anchor" id="3e7fb9ed-3568-4986-9a15-1f1e1893ba1f"></span>
## 2.参数
<p>pQryTransferBank：查询转帐银行</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBankIDType</td>
<td style="TEXT-ALIGN: left;">BankID</td>
<td style="TEXT-ALIGN: left;">银行代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBankBrchIDType</td>
<td style="TEXT-ALIGN: left;">BankBrchID</td>
<td style="TEXT-ALIGN: left;">银行分中心代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="5c5d68e1-20ee-47d3-ae62-f1863f13e715"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ee0be8e7-9b70-4fb5-aa5f-94b77fed7014"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="ec22aae9-b12c-4d31-b39d-6dc2c8139f76"></span>
## 5.FAQ
<p>无</p>
