<p>请求SPBM跨品种抵扣参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMINTERPARAMETER/">OnRspQrySPBMInterParameter</a></p>
<span class="anchor" id="557f62d6-2cda-402b-b7e1-58cb573e3a1a"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMInterParameter(CThostFtdcQrySPBMInterParameterField *pQrySPBMInterParameter, int nRequestID) = 0;</p>
<span class="anchor" id="dcf727bf-9954-40a8-a7d0-8198e2e0b8a8"></span>
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
<span class="anchor" id="ba5fea0d-dd3e-49b8-b83d-3c036f2ca906"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="51d814f3-1da8-4a8f-86c9-2a544e4eeab1"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="2628b3e6-d413-42ad-afb0-6bc62fbdbb6f"></span>
## 5.FAQ
<p>无</p>
