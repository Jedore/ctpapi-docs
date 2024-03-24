<p>请求SPBM品种内对锁仓折扣参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMINTRAPARAMETER/">OnRspQrySPBMIntraParameter</a></p>
<span class="anchor" id="217b50b6-9d17-41e8-a0d3-137aae46b872"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMIntraParameter(CThostFtdcQrySPBMIntraParameterField *pQrySPBMIntraParameter, int nRequestID) = 0;</p>
<span class="anchor" id="28a71e9d-6842-4277-bbb3-1d74b83252ac"></span>
## 2.参数
<p>pQrySPBMIntraParameter：SPBM品种内对锁仓折扣参数查询</p>
<pre><code>struct CThostFtdcQrySPBMIntraParameterField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
};
</code></pre>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">品种代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="a16094da-4209-4108-bb45-753c674c9650"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="8cfde8d3-eb3a-49bd-adde-de1eb8d6f5f9"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="4b43da4b-f591-4c81-ac4e-822f2596ce11"></span>
## 5.FAQ
<p>无</p>
