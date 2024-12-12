<p>请求SPBM附加跨品种抵扣参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMADDONINTERPARAMETER/">OnRspQrySPBMAddOnInterParameter</a></p>
<span class="anchor" id="4e9c4191-d0b4-4043-bca9-347987aab5b3"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMAddOnInterParameter(CThostFtdcQrySPBMAddOnInterParameterField *pQrySPBMAddOnInterParameter, int nRequestID) = 0;</p>
<span class="anchor" id="ad33329d-d0bb-4839-b996-2a2e5c93abca"></span>
## 2.参数
<p>pQrySPBMAddOnInterParameter：SPBM附加跨品种抵扣参数查询</p>
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
<span class="anchor" id="1ada2450-5aaa-48b7-8dc2-f8d7ca7d937d"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="fe7178b5-d6f8-485b-8a9b-e840c757205a"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="c4d3f884-7dbd-42ed-ad91-38a4eb376552"></span>
## 5.FAQ
<p>无</p>
