<p>请求SPBM跨品种抵扣参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMINTERPARAMETER/">OnRspQrySPBMInterParameter</a></p>
<span class="anchor" id="2679a663-8ed2-40da-baef-88dc4bc24a8e"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMInterParameter(CThostFtdcQrySPBMInterParameterField *pQrySPBMInterParameter, int nRequestID) = 0;</p>
<span class="anchor" id="c74d2cf5-b556-464f-a669-b2e15de7b956"></span>
## 2.参数
<p>pQrySPBMInterParameter：SPBM跨品种抵扣参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">Leg1ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">第一腿构成品种</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">Leg2ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">第二腿构成品种</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="e3f0df0a-01ce-4bdd-886d-46d9068c90d9"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="f5a4b8ae-5e71-48d7-a038-bdc012a1e170"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="0705715a-5ff2-4aa5-882a-f2091a5bca61"></span>
## 5.FAQ
<p>无</p>
