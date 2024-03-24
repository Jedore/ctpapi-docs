<p>请求SPBM跨品种抵扣参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMINTERPARAMETER/">OnRspQrySPBMInterParameter</a></p>
<span class="anchor" id="d4b42191-6716-47ca-bfa3-4b9fe202c7aa"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMInterParameter(CThostFtdcQrySPBMInterParameterField *pQrySPBMInterParameter, int nRequestID) = 0;</p>
<span class="anchor" id="1b638fe6-784e-45f5-8f6f-938116224dfa"></span>
## 2.参数
<p>pQrySPBMInterParameter：SPBM跨品种抵扣参数查询</p>
<pre><code>struct CThostFtdcQrySPBMInterParameterField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///第一腿构成品种
    TThostFtdcInstrumentIDType  Leg1ProdFamilyCode;
    ///第二腿构成品种
    TThostFtdcInstrumentIDType  Leg2ProdFamilyCode;
};
</code></pre>
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
<span class="anchor" id="66e49c02-0842-46eb-a63c-5d1d96a336e1"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="4d10b465-57e0-453a-b902-ec5cb14bfca4"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="4c9764ab-12b3-4e3a-b9d0-72202d130303"></span>
## 5.FAQ
<p>无</p>
