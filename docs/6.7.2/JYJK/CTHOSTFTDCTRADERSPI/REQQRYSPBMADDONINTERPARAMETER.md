<p>请求SPBM附加跨品种抵扣参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMADDONINTERPARAMETER/">OnRspQrySPBMAddOnInterParameter</a></p>
<span class="anchor" id="77625fa5-04cd-4b68-aae9-d98a4e038163"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMAddOnInterParameter(CThostFtdcQrySPBMAddOnInterParameterField *pQrySPBMAddOnInterParameter, int nRequestID) = 0;</p>
<span class="anchor" id="cb7e5cb0-5512-4337-822a-3b5b8efed3f0"></span>
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
<span class="anchor" id="9e8540cb-049e-45a9-93d1-e6eeb933e8f7"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="34e5ce64-5812-440b-95ac-6e9cf2cfc927"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="e62315b0-0646-4810-9d56-09ba90e21ac6"></span>
## 5.FAQ
<p>无</p>
