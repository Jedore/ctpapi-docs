<p>请求查询转帐银行</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYTRANSFERBANK/">OnRspQryTransferBank</a></p>
<span class="anchor" id="765f72ec-a49c-49d9-ad7f-e5da3437c2e4"></span>
## 1.函数原型
<p>virtual int ReqQryTransferBank(CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID) = 0;</p>
<span class="anchor" id="642e6e0d-f463-4e46-90c6-00645ca19465"></span>
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
<span class="anchor" id="565905d3-540b-44a3-b12d-91eab2e6bbb0"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="a74d287a-3f4e-49c4-927a-929bada8437b"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="2b0547f9-baa3-4a87-951a-86966e6f6198"></span>
## 5.FAQ
<p>无</p>
