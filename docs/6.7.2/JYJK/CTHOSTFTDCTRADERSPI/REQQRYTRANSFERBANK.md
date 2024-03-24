<p>请求查询转帐银行</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYTRANSFERBANK/">OnRspQryTransferBank</a></p>
<span class="anchor" id="a94bdd60-feff-45c1-84b4-f71647fea470"></span>
## 1.函数原型
<p>virtual int ReqQryTransferBank(CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID) = 0;</p>
<span class="anchor" id="581cced2-b6a7-4459-a231-2d4a3331c147"></span>
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
<span class="anchor" id="1f1bf905-c5c0-4404-9697-ced13ecca652"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="8e89fed6-1478-4fe2-accf-3258777e5f93"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="c8930a4f-9f20-4660-821b-c63f46fff3ca"></span>
## 5.FAQ
<p>无</p>
