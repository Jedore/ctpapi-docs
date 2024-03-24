<p>请求SPBM跨品种抵扣参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMINTERPARAMETER/">OnRspQrySPBMInterParameter</a></p>
<span class="anchor" id="0310c592-1fd4-4dd6-8f59-2ce06e6333dd"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMInterParameter(CThostFtdcQrySPBMInterParameterField *pQrySPBMInterParameter, int nRequestID) = 0;</p>
<span class="anchor" id="73ae683b-acd8-4fb8-8b75-7235daedd938"></span>
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
<span class="anchor" id="4feda1b7-05f9-4dee-a723-e3b68b28a558"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="dba98a5e-7a58-4888-9fce-54c854174ffd"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="0f87c23e-5e47-4c79-b783-8b93e9b3299b"></span>
## 5.FAQ
<p>无</p>
