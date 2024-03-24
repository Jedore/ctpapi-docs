<p>请求查询转帐银行</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYTRANSFERBANK/">OnRspQryTransferBank</a></p>
<span class="anchor" id="2cf4f548-17f8-4537-b3ce-04771d44105c"></span>
## 1.函数原型
<p>virtual int ReqQryTransferBank(CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID) = 0;</p>
<span class="anchor" id="0e636570-42e8-4c35-ad78-e1614e6b127e"></span>
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
<span class="anchor" id="837a2e37-ce95-4bac-9c4d-eec6e81d2b3c"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ea9b3790-cc55-47f3-bda1-afda82f1528d"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="4d8a0047-f738-460c-940c-fe7a637876f7"></span>
## 5.FAQ
<p>无</p>
